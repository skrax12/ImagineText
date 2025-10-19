% ================================
% Facts: People
% ================================
% person(Name, Role, Description) - Defines key individuals involved in the case, their role, and a brief description.
% Example: ?- person(charlie_kirk, Role, Desc). -> Role = victim, Desc = conservative_activist.
person(charlie_kirk, victim, conservative_activist).  % Charlie Kirk: The victim of the assassination.
person(tyler_robinson, suspect, student).  % Tyler Robinson: The suspect, a UVU student.
person(erika_kirk, family, widow).  % Erika Kirk: Charlie's widow and family member.
person(donald_trump, attendee, president).  % Donald Trump: Attended the memorial as President.
person(jd_vance, attendee, vice_president).  % JD Vance: Attended memorial and casket transport as VP.
person(elon_musk, attendee, entrepreneur).  % Elon Musk: Attended the memorial.
person(mike_johnson, attendee, speaker_of_house).  % Mike Johnson: Attended prayer vigil.
person(rfk_jr, attendee, official).  % RFK Jr.: Attended prayer vigil.
person(karoline_leavitt, attendee, official).  % Karoline Leavitt: Attended prayer vigil.
person(cardinal_timothy_dolan, speaker, cardinal).  % Cardinal Timothy Dolan: Gave remarks at memorial.
person(katherine_schweit, expert, former_fbi).  % Katherine Schweit: Former FBI expert on case.
person(tony_graf, judicial, judge).  % Tony Graf: Judge in the court hearing.

% ================================
% Facts: Locations
% ================================
% location(Name, Type, Description) - Defines key sites as "travel stops" with type and description.
% Example: ?- location(utah_valley_university, Type, Desc). -> Type = university, Desc = 'Orem, UT - Site of shooting'.
location(utah_valley_university, university, 'Orem, UT - Site of shooting').  % UVU: Where the shooting and related events occurred.
location(utah_court, judicial, 'Provo, UT - Court hearings').  % Court in Provo: Site of legal proceedings.
location(kennedy_center, vigil, 'Washington, DC - Prayer vigil site').  % Kennedy Center: National prayer vigil location.
location(state_farm_stadium, memorial, 'Glendale, AZ - Main memorial venue').  % State Farm Stadium: Memorial service site.
location(turning_point_usa_hq, organization, 'Phoenix, AZ - TPUSA offices').  % TPUSA HQ: Casket transport destination.
location(fbi_office, investigation, 'Salt Lake City, UT - FBI hub').  % FBI Office: Investigation and arrest site.
location(home_kirk_family, residence, 'Phoenix, AZ - Kirk family home').  % Kirk Family Home: Pre-event residence for Erika Kirk.
location(hotel_provo, lodging, 'Provo, UT - Hotel near UVU for tour prep').  % Provo Hotel: Charlie Kirk's pre-event lodging.
location(home_robinson_family, residence, 'Southwestern Utah - Robinson family home').  % Robinson Family Home: Tyler's pre-event home.
location(uvu_dorm, student_housing, 'Orem, UT - UVU student dorms').  % UVU Dorm: Alternative pre-event for Tyler Robinson.
location(salt_lake_city_utah, city, 'Salt Lake City, UT - General area').  % Salt Lake City: Site of Restaurantology Summit.

% ================================
% Facts: Events
% ================================
% event(EventID, Date, Location, Description) - Defines the timeline of events with date, location, and description.
% Example: ?- event(shooting, Date, Loc, Desc). -> Date = date(2025-09-10), Loc = utah_valley_university, Desc = 'Charlie Kirk assassinated during event'.
event(restaurantology_summit, date(2025-09-10), salt_lake_city_utah, 'Charlie joined Andrew K Smith at the Restaurantology Summit').  % Summit: Pre-shooting event Charlie attended.
event(campus_event, date(2025-09-10), utah_valley_university, 'Charlie Kirk campus event').  % Campus Event: Lead-up to shooting at UVU.
event(shooting, date(2025-09-10), utah_valley_university, 'Charlie Kirk assassinated during event').  % Shooting: The assassination event.
event(manhunt, date(2025-09-11), utah_valley_university, 'FBI manhunt begins; $100k reward offered').  % Manhunt: Immediate post-shooting search.
event(arrest, date(2025-09-12), fbi_office, 'Tyler Robinson arrested after family turns him in').  % Arrest: Suspect captured.
event(local_memorial, date(2025-09-13), utah_valley_university, 'On-campus memorial vigil at UVU').  % Local Memorial: Vigil at UVU.
event(prayer_vigil, date(2025-09-14), kennedy_center, 'National prayer vigil with officials').  % Prayer Vigil: National event in DC.
event(court_hearing, date(2025-09-16), utah_court, 'Initial hearing via video; Judge Tony Graf').  % Court Hearing: Legal proceeding.
event(casket_transport, date(2025-09-20), turning_point_usa_hq, 'Casket arrives in AZ on Air Force Two with JD Vance').  % Casket Transport: Body moved to AZ.
event(main_memorial, date(2025-09-21), state_farm_stadium, 'Memorial service with speeches by Trump, Erika Kirk, etc.').  % Main Memorial: Final service.

% ================================
% Facts: Relationships
% ================================
% at_location(Person, Location) - Indicates a person's presence at a location during events.
% Example: ?- at_location(charlie_kirk, Loc). -> Loc = salt_lake_city_utah ; Loc = utah_valley_university.
at_location(charlie_kirk, salt_lake_city_utah).  % Charlie at Salt Lake City for summit.
at_location(charlie_kirk, utah_valley_university).  % Charlie at UVU for campus event and shooting.
at_location(tyler_robinson, utah_valley_university).  % Tyler at UVU for shooting.
at_location(tyler_robinson, fbi_office).  % Tyler at FBI office post-arrest.
at_location(erika_kirk, utah_valley_university).  % Erika at UVU post-shooting.
at_location(erika_kirk, state_farm_stadium).  % Erika at memorial.
at_location(donald_trump, state_farm_stadium).  % Trump at memorial.
at_location(jd_vance, turning_point_usa_hq).  % Vance at TPUSA HQ for casket.
at_location(jd_vance, state_farm_stadium).  % Vance at memorial.
at_location(elon_musk, state_farm_stadium).  % Musk at memorial.
at_location(mike_johnson, kennedy_center).  % Johnson at prayer vigil.
at_location(rfk_jr, kennedy_center).  % RFK Jr. at prayer vigil.
at_location(karoline_leavitt, kennedy_center).  % Leavitt at prayer vigil.
at_location(cardinal_timothy_dolan, state_farm_stadium).  % Dolan at memorial for remarks.
at_location(tony_graf, utah_court).  % Graf at court hearing.
at_location(fbi, fbi_office).  % FBI at their office.

% attends(Person, Event) - Specifies who attended or participated in specific events.
% Example: ?- attends(charlie_kirk, Event). -> Event = restaurantology_summit ; Event = campus_event.
attends(charlie_kirk, restaurantology_summit).  % Charlie attended the summit.
attends(charlie_kirk, campus_event).  % Charlie attended the campus event.
attends(erika_kirk, local_memorial).  % Erika attended local memorial.
attends(erika_kirk, prayer_vigil).  % Erika attended prayer vigil.
attends(erika_kirk, main_memorial).  % Erika attended main memorial.
attends(donald_trump, main_memorial).  % Trump attended main memorial.
attends(jd_vance, casket_transport).  % Vance attended casket transport.
attends(jd_vance, main_memorial).  % Vance attended main memorial.
attends(elon_musk, main_memorial).  % Musk attended main memorial.
attends(mike_johnson, prayer_vigil).  % Johnson attended prayer vigil.
attends(rfk_jr, prayer_vigil).  % RFK Jr. attended prayer vigil.
attends(karoline_leavitt, prayer_vigil).  % Leavitt attended prayer vigil.
attends(cardinal_timothy_dolan, main_memorial).  % Dolan attended main memorial.

% suspect_of(Person, Event) - Links suspects to events.
% Example: ?- suspect_of(Who, shooting). -> Who = tyler_robinson.
suspect_of(tyler_robinson, shooting).  % Tyler is the suspect in the shooting.

% victim_of(Person, Event) - Links victims to events.
% Example: ?- victim_of(Who, shooting). -> Who = charlie_kirk.
victim_of(charlie_kirk, shooting).  % Charlie is the victim of the shooting.

% charged_with(Person, Charge) - Legal charges against individuals.
% Example: ?- charged_with(tyler_robinson, Charge). -> Charge = first_degree_murder.
charged_with(tyler_robinson, first_degree_murder).  % Tyler charged with murder.

% intends_to_seek(Entity, Action, Against) - Planned legal actions.
% Example: ?- intends_to_seek(prosecutors, death_penalty, Who). -> Who = tyler_robinson.
intends_to_seek(prosecutors, death_penalty, tyler_robinson).  % Prosecutors seek death penalty against Tyler.

% offers_forgiveness(Person, To) - Forgiveness actions by family.
% Example: ?- offers_forgiveness(erika_kirk, To). -> To = tyler_robinson.
offers_forgiveness(erika_kirk, tyler_robinson).  % Erika offers forgiveness to Tyler.

% at_location_before_event(Person, Location, Event) - Positions before a specific event (e.g., shooting).
% Example: ?- at_location_before_event(charlie_kirk, Loc, shooting). -> Loc = hotel_provo ; Loc = salt_lake_city_utah ; Loc = restaurantology_summit.
at_location_before_event(charlie_kirk, hotel_provo, shooting).  % Charlie at Provo hotel before shooting.
at_location_before_event(charlie_kirk, salt_lake_city_utah, shooting).  % Charlie at Salt Lake City before shooting.
at_location_before_event(charlie_kirk, restaurantology_summit, shooting).  % Charlie at summit (treated as location) before shooting.
at_location_before_event(erika_kirk, home_kirk_family, shooting).  % Erika at home before shooting.
at_location_before_event(tyler_robinson, home_robinson_family, shooting).  % Tyler at family home before shooting.
at_location_before_event(tyler_robinson, uvu_dorm, shooting).  % Tyler possibly at dorm before shooting.

% ================================
% Rules: Core Case Queries
% ================================
% involved_in_event(Person, Event) - Determines if a person is involved in an event based on location; excludes post-death for victim.
% Logic: Matches if person is at event's location; for victim, only events on/before shooting date.
% Example: ?- involved_in_event(charlie_kirk, shooting). -> true. (But ?- involved_in_event(charlie_kirk, manhunt). -> false, since post-death).
involved_in_event(Person, Event) :-
    event(Event, Date, Location, _),
    at_location(Person, Location),
    % Exclude events after shooting for the victim
    (victim_of(Person, shooting) ->
        event(shooting, ShootingDate, _, _),
        Date @=< ShootingDate
    ; true).

% qualifies_for_death_penalty(Event, Result) - Checks if an event qualifies for death penalty based on aggravating factors.
% Logic: 'yes' if aggravating factors present; 'no' otherwise.
% Example: ?- qualifies_for_death_penalty(shooting, Result). -> Result = yes.
qualifies_for_death_penalty(shooting, yes) :-
    has_aggravating_factors(shooting, political_assassination).
qualifies_for_death_penalty(shooting, no) :-
    \+ has_aggravating_factors(shooting, _).

% has_aggravating_factors(Event, Factor) - Defines aggravating factors for penalty qualification.
% Example: ?- has_aggravating_factors(shooting, Factor). -> Factor = political_assassination.
has_aggravating_factors(shooting, political_assassination).  % Political nature as aggravating factor.

% event_at(Location, Event) - Finds events at a specific location.
% Logic: Matches events to their locations.
% Example: ?- event_at(utah_valley_university, Event). -> Event = campus_event ; Event = shooting ; Event = manhunt ; Event = local_memorial.
event_at(Location, Event) :-
    event(Event, _, Location, _).

% primary_suspect(Who) - Identifies the primary suspect in the shooting.
% Logic: Matches suspect_of for shooting.
% Example: ?- primary_suspect(Who). -> Who = tyler_robinson.
primary_suspect(Who) :-
    suspect_of(Who, shooting).

% mitigates_penalty(Person, Suspect) - Checks if forgiveness might mitigate penalties.
% Logic: Matches if family member offers forgiveness.
% Example: ?- mitigates_penalty(erika_kirk, tyler_robinson). -> true.
mitigates_penalty(Person, Suspect) :-
    offers_forgiveness(Person, Suspect),
    person(Person, family, _).

% ================================
% Rules: Travel Planner Functionality
% ================================
% full_timeline(Itinerary) - Generates chronological list of all events leading to and including the memorial.
% Logic: Collects events before memorial date, appends memorial.
% Example: ?- full_timeline(Itinerary). -> Itinerary = [restaurantology_summit, campus_event, shooting, manhunt, arrest, local_memorial, prayer_vigil, court_hearing, casket_transport, main_memorial].
full_timeline(Itinerary) :-
    findall(Event, (event(Event, Date, _, _), Date @< date(2025-09-21)), PreEvents),
    append(PreEvents, [main_memorial], Itinerary).

% plan_itinerary(Person, Itinerary) - Builds a personal itinerary including pre-events and attended/involved events, excluding duplicates.
% Logic: Collects pre-locations as pre_event(PreLoc), then events (attends or involved), excluding those marked as pre-event; sorts by date.
% Example: ?- plan_itinerary(charlie_kirk, Itinerary). -> Itinerary = [pre_event(hotel_provo), pre_event(salt_lake_city_utah), pre_event(restaurantology_summit), campus_event, shooting].
plan_itinerary(Person, Itinerary) :-
    % Collect pre-event locations for shooting
    findall(PreLoc, at_location_before_event(Person, PreLoc, shooting), PreLocs),
    % Collect events, excluding those that are pre-event locations
    findall(Event, (
        (attends(Person, Event); involved_in_event(Person, Event)),
        \+ (at_location_before_event(Person, Event, shooting))
    ), Events),
    % Add pre-event locations as pre_event(Location)
    findall(pre_event(PreLoc), member(PreLoc, PreLocs), PreStops),
    append(PreStops, Events, TempItin),
    sort_by_date(TempItin, Itinerary).

% sort_by_date(Events, Sorted) - Helper rule to sort events and pre-events by date.
% Logic: Assigns pre-events an early date (2025-09-09), pairs with actual dates, sorts pairs, extracts sorted list.
% Example: (Internal helper; not directly queryable, but used in plan_itinerary).
sort_by_date(Events, Sorted) :-
    findall((Date, Event), (
        member(Event, Events),
        (Event = pre_event(_) -> Date = date(2025-09-09); event(Event, Date, _, _))
    ), Pairs),
    sort(Pairs, SortedPairs),
    findall(E, (member((_, E), SortedPairs)), Sorted).

% path_to_memorial(StartLoc, EndLoc, Path) - Builds a location-based path from start to memorial.
% Logic: Collects all event locations (excluding end), appends start and end.
% Example: ?- path_to_memorial(utah_valley_university, state_farm_stadium, Path). -> Path = [utah_valley_university, fbi_office, utah_court, kennedy_center, turning_point_usa_hq, state_farm_stadium].
path_to_memorial(StartLoc, EndLoc, Path) :-
    location(StartLoc, _, _),
    location(EndLoc, memorial, _),
    findall(Loc, (at_location(_, Loc), event(_, _, Loc, _), Loc \= EndLoc), AllLocs),
    append([StartLoc], AllLocs, TempPath),
    append(TempPath, [EndLoc], Path).

% pre_event_locations(Event, List) - Collects all pre-event locations for people before a specific event.
% Logic: Finds all (Person, Location) pairs before the event.
% Example: ?- pre_event_locations(shooting, List). -> List = [(charlie_kirk, hotel_provo), (charlie_kirk, salt_lake_city_utah), (charlie_kirk, restaurantology_summit), (erika_kirk, home_kirk_family), (tyler_robinson, home_robinson_family), (tyler_robinson, uvu_dorm)].
pre_event_locations(Event, List) :-
    findall((Person, Location), at_location_before_event(Person, Location, Event), List).