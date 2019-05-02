#
# PySNMP MIB module Juniper-PPPOE-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-PPPOE-PROFILE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:03:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, JuniSetMap = mibBuilder.importSymbols("Juniper-TC", "JuniEnable", "JuniSetMap")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, MibIdentifier, Integer32, Gauge32, iso, Counter32, TimeTicks, Unsigned32, Counter64, NotificationType, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibIdentifier", "Integer32", "Gauge32", "iso", "Counter32", "TimeTicks", "Unsigned32", "Counter64", "NotificationType", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniPppoeProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46))
juniPppoeProfileMIB.setRevisions(('2008-06-18 10:29', '2005-07-13 11:40', '2004-06-10 19:25', '2003-03-11 21:58', '2002-09-16 21:44', '2002-08-15 20:34', '2002-08-15 19:07', '2001-03-21 18:32',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniPppoeProfileMIB.setRevisionsDescriptions(('Added juniPppoeProfileMaxSessionOverride object.', 'Added MTU control object.', 'Added Remote Circuit Id Capture object.', 'Added Service Name Table object.', 'Replaced Unisphere names with Juniper names.', 'Added PADI flag and packet trace support.', 'Added duplicate MAC address indicator and AC-NAME tag objects.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniPppoeProfileMIB.setLastUpdated('200806181029Z')
if mibBuilder.loadTexts: juniPppoeProfileMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniPppoeProfileMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniPppoeProfileMIB.setDescription('The point-to-point protocol over Ethernet (PPPoE) profile MIB for the Juniper enterprise.')
juniPppoeProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1))
juniPppoeProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1))
juniPppoeProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1), )
if mibBuilder.loadTexts: juniPppoeProfileTable.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileTable.setDescription('This table contains profiles for configuring PPPoE interfaces/sessions. Entries in this table are created/deleted as a side-effect of corresponding operations to the juniProfileNameTable in the Juniper-PROFILE-MIB.')
juniPppoeProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileId"))
if mibBuilder.loadTexts: juniPppoeProfileEntry.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileEntry.setDescription('A profile describing configuration of a PPPoE interface and its subinterfaces (sessions).')
juniPppoeProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniPppoeProfileId.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileId.setDescription('The integer identifier associated with this profile. A value for this identifier is determined by locating or creating a profile name in the juniProfileNameTable.')
juniPppoeProfileSetMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 2), JuniSetMap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileSetMap.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileSetMap.setDescription("A bitmap representing which objects in this entry have been explicitly configured. See the definition of the JuniSetMap TEXTUAL-CONVENTION for details of use. The INDEX object(s) and this object are excluded from representation (i.e. their bits are never set). When a SET request does not explicitly configure JuniSetMap, bits in JuniSetMap are set as a side-effect of configuring other profile attributes in the same entry. If, however, a SET request explicitly configures JuniSetMap, the explicitly configured value overrides 1) any previous bit settings, and 2) any simultaneous 'side-effect' settings that would otherwise occur. Once set, bits can only be cleared by explicitly configuring JuniSetMap.")
juniPppoeProfileMaxNumSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileMaxNumSessions.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileMaxNumSessions.setDescription('The maximum number of PPPoE sessions (subinterfaces) that can be configured on the main PPPoE interface created using this profile. A value of zero indicates no bound is configured.')
juniPppoeProfileSubMotm = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileSubMotm.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileSubMotm.setDescription('A message to send via a PADM on the sub-interface when this profile is applied to the IP interface above this PPPoE sub- interface. A client may choose to display this message to the user.')
juniPppoeProfileSubUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileSubUrl.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileSubUrl.setDescription('A URL to be sent via a PADM on the sub-interface when this profile is applied to the IP interface above this PPPoE sub-interface. The string entered here can have several substitutions applied: %D is replaced with the profile name %d is replaced with the domain name %u is replaced with the user name %U is replaced with the user/domain name together %% is replaced with the % character The resulting string must not be greater than 127 octets long. The client may use this URL as the initial web-page for the user.')
juniPppoeProfileDupProtect = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 6), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileDupProtect.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileDupProtect.setDescription('Flag to control whether duplicate MAC addresses are allowed')
juniPppoeProfileAcName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileAcName.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileAcName.setDescription('The name to use for the AC-NAME tag that is sent in any PADO that is sent on this interface.')
juniPppoeProfilePadiFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 8), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfilePadiFlag.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfilePadiFlag.setDescription('The PPPoE major interface parameter PADI flag controls whether to always repsond to a PADI with a PADO regardless of the ability to create the session and allow the session establish phase to resolve it.')
juniPppoeProfilePacketTrace = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 9), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfilePacketTrace.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfilePacketTrace.setDescription('The PPPoE major interface parameter packet tracing flag controls whether packet tracing is enable or not.')
juniPppoeProfileServiceNameTableName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileServiceNameTableName.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileServiceNameTableName.setDescription('The PPPoE Service name table controls behavior of PADO control packets.')
juniPppoeProfilePadrRemoteCircuitIdCapture = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 11), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfilePadrRemoteCircuitIdCapture.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfilePadrRemoteCircuitIdCapture.setDescription('The PPPoE major interface parameter PADR remote circuit id capture flag controls whether the remote circuit id string possibly contained in the PADR packet will be saved and used by AAA to replace the NAS-PORT-ID field.')
juniPppoeProfileMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ValueRangeConstraint(66, 65535), )).clone(1494)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileMtu.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileMtu.setDescription('The initial Maximum Transmit Unit (MTU) that the PPPoE major interface entity will advertise to the remote entity. If the value of this variable is 1 then the local PPPoE entity will use an MTU value determined by its underlying media interface. If the value of this variable is 2 then the local PPPoE entity will use a value determined by the PPPoE Max-Mtu-Tag transmitted from the client in the PADR packet. If no Max-Mtu-Tag is received, the value defaults to a maximum of 1494. The operational MTU is limited by the MTU of the underlying media interface minus the PPPoE frame overhead.')
juniPppoeProfileMaxSessionOverride = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("override", 1), ("ignore", 2))).clone('ignore')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileMaxSessionOverride.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileMaxSessionOverride.setDescription('Configure the action to be taken by PPPoE when RADIUS server returns the PPPoE max-session value: override Override the current PPPoE max-session value with the value returned by RADIUS server Ignore Ignore the max-session value returned by RADIUS server')
juniPppoeProfileConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4))
juniPppoeProfileCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1))
juniPppoeProfileGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2))
juniPppoeProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 1)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileCompliance = juniPppoeProfileCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileCompliance.setDescription('Obsolete compliance statement for entities which implement the Juniper PPPoE Profile MIB. This statement became obsolete when the duplicate MAC address indicator and AC-NAME tag were added.')
juniPppoeCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 2)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance2 = juniPppoeCompliance2.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeCompliance2.setDescription('Obsolete compliance statement for entities which implement the Juniper PPPoE profile MIB. This statement became obsolete when PADI flag, AC-name and packet trace objects were added.')
juniPppoeCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 3)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance3 = juniPppoeCompliance3.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeCompliance3.setDescription('Obsolete compliance statement for entities which implement the Juniper PPPoE profile MIB. This statement became obsolete when the service name table was added.')
juniPppoeCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 4)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance4 = juniPppoeCompliance4.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeCompliance4.setDescription('Obsolete compliance statement for entities which implement the Juniper PPPoE profile MIB. This statement became obsolete when the remote circuit id capture was added.')
juniPppoeCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 5)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance5 = juniPppoeCompliance5.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeCompliance5.setDescription('Obsolete compliance statement for entities which implement the Juniper PPPoE MIB. This statement became obsolete when support was added for MTU configuration.')
juniPppoeCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 6)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup6"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance6 = juniPppoeCompliance6.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeCompliance6.setDescription('Obsolete compliance statement for entities which implement the Juniper PPPoE MIB. This statement became obsolete when support was added for juniPppoeProfileMaxSessionOverride.')
juniPppoeCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 7)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup7"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance7 = juniPppoeCompliance7.setStatus('current')
if mibBuilder.loadTexts: juniPppoeCompliance7.setDescription('The compliance statement for entities which implement the Juniper PPPoE Profile MIB.')
juniPppoeProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 1)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup = juniPppoeProfileGroup.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileGroup.setDescription('Obsolete collection of objects providing management of profile functionality for PPPoE interfaces in a Juniper product. This group became obsolete when the duplicate MAC address indicator and AC-NAME tag objects were added.')
juniPppoeProfileGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 2)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup2 = juniPppoeProfileGroup2.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileGroup2.setDescription('Obsolete collection of objects providing management of profile functionality for PPPOE interfaces in a Juniper product. This group became obsolete when PADI flag, AC-name and packet trace objects were added.')
juniPppoeProfileGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 3)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup3 = juniPppoeProfileGroup3.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileGroup3.setDescription('A collection of objects providing management of profile functionality for PPPOE interfaces in a Juniper product.')
juniPppoeProfileGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 4)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup4 = juniPppoeProfileGroup4.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileGroup4.setDescription('A collection of objects providing management of profile functionality for PPPOE interfaces in a Juniper product.')
juniPppoeProfileGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 5)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadrRemoteCircuitIdCapture"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup5 = juniPppoeProfileGroup5.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileGroup5.setDescription('A collection of objects providing management of profile functionality for PPPOE interfaces in a Juniper product.')
juniPppoeProfileGroup6 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 6)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadrRemoteCircuitIdCapture"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMtu"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup6 = juniPppoeProfileGroup6.setStatus('obsolete')
if mibBuilder.loadTexts: juniPppoeProfileGroup6.setDescription('A collection of objects providing management of profile functionality for PPPOE interfaces in a Juniper product.')
juniPppoeProfileGroup7 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 7)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadrRemoteCircuitIdCapture"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMtu"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxSessionOverride"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup7 = juniPppoeProfileGroup7.setStatus('current')
if mibBuilder.loadTexts: juniPppoeProfileGroup7.setDescription('A collection of objects providing management of profile functionality for PPPOE interfaces in a Juniper product.')
mibBuilder.exportSymbols("Juniper-PPPOE-PROFILE-MIB", juniPppoeCompliance5=juniPppoeCompliance5, juniPppoeProfileGroup2=juniPppoeProfileGroup2, juniPppoeProfileMtu=juniPppoeProfileMtu, juniPppoeProfile=juniPppoeProfile, juniPppoeProfileSetMap=juniPppoeProfileSetMap, juniPppoeProfilePadiFlag=juniPppoeProfilePadiFlag, juniPppoeProfileTable=juniPppoeProfileTable, juniPppoeProfileDupProtect=juniPppoeProfileDupProtect, juniPppoeCompliance4=juniPppoeCompliance4, juniPppoeProfileGroup=juniPppoeProfileGroup, juniPppoeProfileMIB=juniPppoeProfileMIB, juniPppoeProfileGroup4=juniPppoeProfileGroup4, juniPppoeProfileCompliances=juniPppoeProfileCompliances, juniPppoeProfileAcName=juniPppoeProfileAcName, juniPppoeProfileGroup3=juniPppoeProfileGroup3, juniPppoeProfilePadrRemoteCircuitIdCapture=juniPppoeProfilePadrRemoteCircuitIdCapture, juniPppoeProfileSubMotm=juniPppoeProfileSubMotm, juniPppoeProfilePacketTrace=juniPppoeProfilePacketTrace, juniPppoeProfileEntry=juniPppoeProfileEntry, juniPppoeProfileGroup5=juniPppoeProfileGroup5, juniPppoeProfileMaxSessionOverride=juniPppoeProfileMaxSessionOverride, juniPppoeCompliance2=juniPppoeCompliance2, juniPppoeProfileGroups=juniPppoeProfileGroups, juniPppoeCompliance6=juniPppoeCompliance6, juniPppoeProfileCompliance=juniPppoeProfileCompliance, juniPppoeCompliance3=juniPppoeCompliance3, juniPppoeCompliance7=juniPppoeCompliance7, juniPppoeProfileGroup6=juniPppoeProfileGroup6, juniPppoeProfileMaxNumSessions=juniPppoeProfileMaxNumSessions, juniPppoeProfileId=juniPppoeProfileId, juniPppoeProfileConformance=juniPppoeProfileConformance, PYSNMP_MODULE_ID=juniPppoeProfileMIB, juniPppoeProfileObjects=juniPppoeProfileObjects, juniPppoeProfileServiceNameTableName=juniPppoeProfileServiceNameTableName, juniPppoeProfileSubUrl=juniPppoeProfileSubUrl, juniPppoeProfileGroup7=juniPppoeProfileGroup7)
