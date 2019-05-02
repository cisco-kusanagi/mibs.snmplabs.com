#
# PySNMP MIB module Juniper-HTTP-Profile-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-HTTP-Profile-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:02:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniSetMap, = mibBuilder.importSymbols("Juniper-TC", "JuniSetMap")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, ModuleIdentity, MibIdentifier, Unsigned32, Integer32, Gauge32, IpAddress, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Integer32", "Gauge32", "IpAddress", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniHttpProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79))
juniHttpProfileMIB.setRevisions(('2005-08-19 14:21',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniHttpProfileMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniHttpProfileMIB.setLastUpdated('200508191421Z')
if mibBuilder.loadTexts: juniHttpProfileMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniHttpProfileMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniHttpProfileMIB.setDescription('The HTTP rofile MIB for the Juniper Networks, Inc. enterprise.')
juniHttpProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1))
juniHttpProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1))
juniHttpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1), )
if mibBuilder.loadTexts: juniHttpProfileTable.setStatus('current')
if mibBuilder.loadTexts: juniHttpProfileTable.setDescription('This table contains profiles for configuring bulk ATM circuits. Entries in this table are created/deleted as a side-effect of corresponding operations to the juniProfileNameTable in the Juniper-PROFILE-MIB.')
juniHttpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-HTTP-Profile-MIB", "juniHttpProfileId"))
if mibBuilder.loadTexts: juniHttpProfileEntry.setStatus('current')
if mibBuilder.loadTexts: juniHttpProfileEntry.setDescription('A profile describing VCC configuration of an ATM subinterface.')
juniHttpProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniHttpProfileId.setStatus('current')
if mibBuilder.loadTexts: juniHttpProfileId.setDescription('The integer identifier associated with this profile. A value for this identifier is determined by locating or creating a profile name in the juniProfileNameTable.')
juniHttpProfileSetMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 2), JuniSetMap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniHttpProfileSetMap.setStatus('current')
if mibBuilder.loadTexts: juniHttpProfileSetMap.setDescription("A bitmap representing which objects in this entry have been explicitly configured. See the definition of the JuniSetMap TEXTUAL-CONVENTION for details of use. The INDEX object(s) and this object are excluded from representation (i.e. their bits are never set). When a SET request does not explicitly configure JuniSetMap, bits in JuniSetMap are set as a side-effect of configuring other profile attributes in the same entry. If, however, a SET request explicitly configures JuniSetMap, the explicitly configured value overrides 1) any previous bit settings, and 2) any simultaneous 'side-effect' settings that would otherwise occur. Once set, bits can only be cleared by explicitly configuring JuniSetMap.")
juniHttpProfileRedirectUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniHttpProfileRedirectUrl.setStatus('current')
if mibBuilder.loadTexts: juniHttpProfileRedirectUrl.setDescription('This object is a 64 byte string that will be used as the redirect URL when requests arrive at the HTTP server over the Ip Interface configured.')
juniHttpProfileConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4))
juniHttpProfileCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 1))
juniHttpProfileGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 2))
juniHttpProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 1, 1)).setObjects(("Juniper-HTTP-Profile-MIB", "juniHttpProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHttpProfileCompliance = juniHttpProfileCompliance.setStatus('current')
if mibBuilder.loadTexts: juniHttpProfileCompliance.setDescription('Compliance statement for entities which implement the Juniper HTTP Profile MIB.')
juniHttpProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 79, 4, 2, 1)).setObjects(("Juniper-HTTP-Profile-MIB", "juniHttpProfileSetMap"), ("Juniper-HTTP-Profile-MIB", "juniHttpProfileRedirectUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHttpProfileGroup = juniHttpProfileGroup.setStatus('current')
if mibBuilder.loadTexts: juniHttpProfileGroup.setDescription('Current collection of objects providing management of profile functionality for per Interface HTTP objects in a Juniper product.')
mibBuilder.exportSymbols("Juniper-HTTP-Profile-MIB", juniHttpProfileSetMap=juniHttpProfileSetMap, juniHttpProfileGroups=juniHttpProfileGroups, juniHttpProfile=juniHttpProfile, juniHttpProfileCompliances=juniHttpProfileCompliances, juniHttpProfileCompliance=juniHttpProfileCompliance, juniHttpProfileRedirectUrl=juniHttpProfileRedirectUrl, juniHttpProfileTable=juniHttpProfileTable, juniHttpProfileMIB=juniHttpProfileMIB, PYSNMP_MODULE_ID=juniHttpProfileMIB, juniHttpProfileId=juniHttpProfileId, juniHttpProfileConformance=juniHttpProfileConformance, juniHttpProfileGroup=juniHttpProfileGroup, juniHttpProfileEntry=juniHttpProfileEntry, juniHttpProfileObjects=juniHttpProfileObjects)
