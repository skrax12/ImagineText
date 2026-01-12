% ================================
% Facts: People (Unchanged)
% ================================
% person(Name, Role, Description) - Defines key individuals involved in the case, their role, and a brief description.
% Example: ?- person(charlie_kirk, Role, Desc). -> Role = victim, Desc = conservative_activist.
person(charlie_kirk, victim, conservative_activist).  % Charlie Kirk: The victim of the assassination.
person(tyler_robinson, suspect, student).  % Tyler Robinson: The suspect, a UVU student.
person(erika_kirk, family, widow).  % Erika Kirk: Charlie's widow and family member; gave multiple interviews.
person(robert_kirk, family, father).  % Robert Kirk: Charlie's father, attended memorial.
person(diane_kirk, family, mother).  % Diane Kirk: Charlie's mother, attended memorial.
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
% Facts: Locations (Minor Addition for Interviews)
% ================================
% location(Name, Type, Description) - Defines key sites as "travel stops" with type and description.
% Example: ?- location(utah_valley_university, Type, Desc). -> Type = university, Desc = 'Orem, UT - Site of shooting'.
location(utah_valley_university, university, 'Orem, UT - Site of shooting').  % UVU: Where the shooting and related events occurred.
location(utah_court, judicial, 'Provo, UT - Court hearings').  % Court in Provo: Site of legal proceedings (including Dec 11 hearing).
location(kennedy_center, vigil, 'Washington, DC - Prayer vigil site').  % Kennedy Center: National prayer vigil location.
location(state_farm_stadium, memorial, 'Glendale, AZ - Main memorial venue').  % State Farm Stadium: Memorial service site.
location(turning_point_usa_hq, organization, 'Phoenix, AZ - TPUSA offices').  % TPUSA HQ: Casket transport destination.
location(fbi_office, investigation, 'Salt Lake City, UT - FBI hub').  % FBI Office: Investigation and arrest site.
location(home_kirk_family, residence, 'Phoenix, AZ - Kirk family home').  % Kirk Family Home: Pre-event residence for Erika Kirk.
location(home_kirk_parents, residence, 'Wheeling, IL - Kirk parents home').  % Kirk Parents Home: Pre-event residence for Robert and Diane Kirk.
location(hotel_provo, lodging, 'Provo, UT - Hotel near UVU for tour prep').  % Provo Hotel: Charlie Kirk's pre-event lodging.
location(home_robinson_family, residence, 'Southwestern Utah - Robinson family home').  % Robinson Family Home: Tyler's pre-event home.
location(uvu_dorm, student_housing, 'Orem, UT - UVU student dorms').  % UVU Dorm: Alternative pre-event for Tyler Robinson.
location(salt_lake_city_utah, city, 'Salt Lake City, UT - General area').  % Salt Lake City: Site of Restaurantology Summit.
location(white_house_rose_garden, ceremony, 'Washington, DC - Site of Medal of Freedom award').  % White House Rose Garden: Medal ceremony location.
location(media_outlet_virtual, interview, 'Virtual/Media - Location for interviews/statements').  % Virtual: For TV/radio/podcast interviews.

% ================================
% Facts: Events (Unchanged + Recent)
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
event(court_hearing_initial, date(2025-09-16), utah_court, 'Initial hearing via video; Judge Tony Graf').  % Initial Court Hearing.
event(casket_transport, date(2025-09-20), turning_point_usa_hq, 'Casket arrives in AZ on Air Force Two with JD Vance').  % Casket Transport: Body moved to AZ.
event(main_memorial, date(2025-09-21), state_farm_stadium, 'Memorial service with speeches by Trump, Erika Kirk, etc.').  % Main Memorial: Final service.
event(medal_of_freedom_ceremony, date(2025-10-14), white_house_rose_garden, 'Posthumous Presidential Medal of Freedom awarded to Charlie Kirk by Trump').  % Medal Ceremony: On Charlie's would-be 32nd birthday.
event(court_hearing_in_person, date(2025-12-11), utah_court, 'Tyler Robinson first in-person appearance; media access debated').  % Recent Hearing: Gag order clarified, next on Jan 16, 2026.

% ================================
% New Facts: Interviews
% ================================
% interview(Person, Date, Outlet, Description) - Tracks notable interviews or public statements.
% Example: ?- interview(erika_kirk, _, fox_news, Desc). -> Desc = 'First interview after assassination with Jesse Watters; discussed last moments and forgiveness'.
interview(charlie_kirk, date(2025-09-07), cnn_tokyo, 'Last interview in Tokyo; discussed Japan far-right and common ground').  % Pre-death: CNN in Tokyo.
interview(charlie_kirk, date(2025-06-29), iced_coffee_hour, 'Resurfaced legacy interview; reflected on how he wanted to be remembered for courage in faith').  % Pre-death resurfaced post-assassination.
interview(erika_kirk, date(2025-11-05), fox_news_jesse_watters, 'First interview after assassination; emotional details on hospital visit, smirk on Charlie\'s face meaning "you got my body, not my soul"').  % First post-death interview.
interview(erika_kirk, date(2025-11-06), fox_news, 'Recalled last moments with Charlie; described assassination as "horror movie"').  % Fox News on final night.
interview(erika_kirk, date(2025-12-04), fox_news_hannity, 'Book tour launch for "Stop, in the Name of God"; discussed carrying on mission').  % Book tour interviews.
interview(erika_kirk, date(2025-12-13), cbs_news_town_hall, 'Town hall with Bari Weiss; addressed conspiracy theories, forgiveness, and people celebrating death ("you\'re sick")').  % CBS town hall on conspiracies.
interview(tyler_robinson_mother, date(2025-09-16), court_documents_media, 'Mother (Amber) on Tyler\'s political shift to left, pro-gay/trans rights, relationship with transitioning roommate').  % Via court docs/interviews.
interview(tyler_robinson_father, date(2025-09-15), ksl_tv, 'Father (Matt) regretted being "too hard" on son during upbringing; discussed mental health').  % KSL-TV interview.
interview(eyewitnesses, date(2025-09-12), youtube_media, 'Eyewitness accounts of the assassination').  % Various eyewitness interviews.
interview(donald_trump, date(2025-10-14), white_house_ceremony, 'Speech at Medal of Freedom; praised Charlie as "fearless warrior," made remarks about enemies').  % Medal ceremony speech.

% ================================
% Facts: Relationships (Updated for Interviews)
% ================================
% at_location(Person, Location) - Indicates a person's presence at a location during events (added virtual for interviews).
at_location(erika_kirk, media_outlet_virtual).  % Erika in multiple interviews.
at_location(tyler_robinson_mother, media_outlet_virtual).  % Family statements via media/court.
at_location(tyler_robinson_father, media_outlet_virtual).

% attends(Person, Event) - Updated to include interview-related if tied to events.
attends(erika_kirk, medal_of_freedom_ceremony).  % Erika accepted Medal and spoke.

% Other relationships unchanged...

% ================================
% Rules: New - Interview Queries
% ================================
% gave_interview(Person, Outlet, Topic) - Queries interviews by person, outlet, or topic (partial match).
% Logic: Matches interview facts; Topic uses sub_atom for partial description match.
% Example: ?- gave_interview(erika_kirk, _, Topic). -> Lists Erika's interviews with topics.
gave_interview(Person, Outlet, Description) :-
    interview(Person, _, Outlet, Description).

% gave_interview_about(Person, Keyword) - Finds interviews containing a keyword in description.
% Example: ?- gave_interview_about(erika_kirk, forgiveness). -> Matches interviews mentioning forgiveness/conspiracies.
gave_interview_about(Person, Keyword) :-
    interview(Person, _, _, Desc),
    sub_atom(Desc, _, Keyword, _).

% ================================
% Other Rules (Unchanged, with minor timeline sort improvement)
% ================================
% ... (Previous rules for involved_in_event, plan_itinerary, full_timeline, etc., remain the same)

% Example Queries for Interviews
% Query 1: Erika Kirk's interviews
% ?- interview(erika_kirk, Date, Outlet, Desc).
% Expected: Lists her Fox News (Watters, Hannity), CBS town hall, etc.

% Query 2: Interviews about conspiracy theories
% ?- gave_interview_about(erika_kirk, conspiracy).
% Expected: CBS town hall interview.

% Query 3: Family statements (Robinson)
% ?- interview(tyler_robinson_mother, _, _, Desc).
% Expected: Mother's comments on political shift.

% Query 4: Integrate into itinerary (manual extension possible via custom query)
% Example: Extend plan_itinerary to include interviews post-shooting for survivors.