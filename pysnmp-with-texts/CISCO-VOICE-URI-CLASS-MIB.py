#
# PySNMP MIB module CISCO-VOICE-URI-CLASS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-URI-CLASS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, iso, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, IpAddress, Counter32, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "iso", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "IpAddress", "Counter32", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
ciscoVoiceUriClassMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 99999999))
ciscoVoiceUriClassMIB.setRevisions(('2002-10-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setLastUpdated('200210100000Z')
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setDescription("This MIB provides information about Voice URI classes that are used to select Dial Peers based on URI's. A Voice URI class contains a set of configurations that is used to match a Voice URI. URI - Uniform Resource Indicator URL - Uniform Resource Locator regex - regular expression RFC 2543 - SIP: Session Initiation Protocol RFC 2806 - URLs for Telephone Calls")
class CvUriClassTagIndex(TextualConvention, OctetString):
    description = 'A Voice URI class tag. This is a value used to uniquely identify each Voice URI class in the system.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class CvUriClassTag(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the CvUriClassTagIndex convention. This extension allows zero-length strings to be used for tags. Examples of usage of zero-length strings as tags might include situations where none of the Voice URI classes need to be referenced.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvUriClassPattern(TextualConvention, OctetString):
    description = 'A regular expression pattern that is configured in the voice URI classes. The default value is a zero-length string. Any pattern set to this default value is not used for matching with the URI'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvUriClassPreference(TextualConvention, Integer32):
    description = 'Preference for a field in the URI. Lower number indicates higher preference. The preference is used to break ties when more than one class matches a given URI. The class, which has the longest match for a field with the highest preference is given higher priority.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 10)

cvUriClassMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 0))
cvUriClassMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1))
cvUriClass = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1))
cvUriClassSIPGeneralConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2))
cvUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1), )
if mibBuilder.loadTexts: cvUriClassCfgTable.setStatus('current')
if mibBuilder.loadTexts: cvUriClassCfgTable.setDescription('The table contains generic Voice URI class information.')
cvUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvUriClassCfgEntry.setStatus('current')
if mibBuilder.loadTexts: cvUriClassCfgEntry.setDescription("A single Voice URI class. The creation of this entry will result in the automatic creation of a corresponding 'cvUriClassCfgType' URI class entry and a cvCommonUriClassCfgEntry.")
cvUriClassCfgTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 1), CvUriClassTagIndex())
if mibBuilder.loadTexts: cvUriClassCfgTag.setStatus('current')
if mibBuilder.loadTexts: cvUriClassCfgTag.setDescription('A name that uniquely identifies a Voice URI class in the system.')
cvUriClassCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sip", 1), ("tel", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvUriClassCfgType.setStatus('current')
if mibBuilder.loadTexts: cvUriClassCfgType.setDescription("Specifies the type of Voice URI class. The type is the schema of the URI's, which this class is configured to match. sip - Voice URI class to match sip: URI's (RFC 2543) tel - Voice URI class to match tel: URI's (RFC 2806) Once created this object cannot be modified.")
cvUriClassCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvUriClassCfgStatus.setStatus('current')
if mibBuilder.loadTexts: cvUriClassCfgStatus.setDescription('This object is used to create, modify or delete a row in this table. A row can be deleted or modified regardless of its current state. When the row is created with createAndWait, it is placed in notInService state, until such time when either the state is changed to active, or the row is deleted.')
cvSIPUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2), )
if mibBuilder.loadTexts: cvSIPUriClassCfgTable.setStatus('current')
if mibBuilder.loadTexts: cvSIPUriClassCfgTable.setDescription('The table contains information related to sip: schema-specific Voice URI classes.')
cvSIPUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvSIPUriClassCfgEntry.setStatus('current')
if mibBuilder.loadTexts: cvSIPUriClassCfgEntry.setDescription('A single sip: schema-specific Voice URI class. This entry is created automatically when a cvUriClassCfgEntry of cvUriClassCfgType(1) is created. The manager cannot create this entry.')
cvSIPUriClassCfgUserIDPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 1), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgUserIDPattern.setStatus('current')
if mibBuilder.loadTexts: cvSIPUriClassCfgUserIDPattern.setDescription('A regular expression to match the user-id in a sip: URI. If this object is set to a zero-length string it is not used for matching with the URI. This object cannot be set if cvCommonUriClassCfgURIPattern is also set.')
cvSIPUriClassCfgHostPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 2), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgHostPattern.setStatus('current')
if mibBuilder.loadTexts: cvSIPUriClassCfgHostPattern.setDescription('A regular expression to match the host portion in a sip: URI. If this object is set to a zero-length string it is not used for matching with the URI. This object cannot be set if cvCommonUriClassCfgURIPattern is also set.')
cvSIPUriClassCfgPhoneCtxtPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 3), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgPhoneCtxtPattern.setStatus('current')
if mibBuilder.loadTexts: cvSIPUriClassCfgPhoneCtxtPattern.setDescription('A regular expression to match the phone-context attribute in a sip: URI. If this object is set to a zero-length string it is not used for matching with the URI. This object cannot be set if cvCommonUriClassCfgURIPattern is also set.')
cvTELUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3), )
if mibBuilder.loadTexts: cvTELUriClassCfgTable.setStatus('current')
if mibBuilder.loadTexts: cvTELUriClassCfgTable.setDescription('The table contains information related to tel: schema-specific Voice URI classes.')
cvTELUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvTELUriClassCfgEntry.setStatus('current')
if mibBuilder.loadTexts: cvTELUriClassCfgEntry.setDescription('A single sip: schema-specific Voice URI class. This entry is created automatically when a cvUriClassCfgEntry of cvUriClassCfgType(2) is created. The manager cannot create this entry.')
cvTELUriClassCfgPhoneNumPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 1), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneNumPattern.setStatus('current')
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneNumPattern.setDescription('A regular expression to match the phone number portion in a tel: URI. If this object is set to a zero-length string it is not used for matching with the URI. This object cannot be set if cvCommonUriClassCfgURIPattern is also set.')
cvTELUriClassCfgPhoneCtxtPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 2), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneCtxtPattern.setStatus('current')
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneCtxtPattern.setDescription('A regular expression to match the phone-context attribute in a tel: URI. If this object is set to a zero-length string it is not used for matching with the URI. This object cannot be set if cvCommonUriClassCfgURIPattern is also set.')
cvCommonUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4), )
if mibBuilder.loadTexts: cvCommonUriClassCfgTable.setStatus('current')
if mibBuilder.loadTexts: cvCommonUriClassCfgTable.setDescription('The table contains common configuration information specific to the Voice URI classes.')
cvCommonUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvCommonUriClassCfgEntry.setStatus('current')
if mibBuilder.loadTexts: cvCommonUriClassCfgEntry.setDescription('A single sip: schema-specific Voice URI class. This entry is created automatically when a cvUriClassCfgEntry is created. The manager cannot create this entry.')
cvCommonUriClassCfgURIPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvCommonUriClassCfgURIPattern.setStatus('current')
if mibBuilder.loadTexts: cvCommonUriClassCfgURIPattern.setDescription('A regular expression to match an entire URI. If this object is set to a zero-length string it is not used for matching with the URI. This object is mutually exclusive with patterns that match specific fields from the URI e.g., cvSIPUriClassCfgUserIDPattern, or cvSIPUriClassCfgPhonePattern. If more than one class matches a URI, the classes that matched with the URI based on this pattern, are given the least priority amongst matching classes.')
cvUriClassSIPHostPreference = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 1), CvUriClassPreference().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvUriClassSIPHostPreference.setStatus('current')
if mibBuilder.loadTexts: cvUriClassSIPHostPreference.setDescription('Preference assigned to the match length resulting from a match of cvSIPUriClassCfgHostPattern against the host portion of a sip: URI.')
cvUriClassSIPUserIDPreference = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 2), CvUriClassPreference().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvUriClassSIPUserIDPreference.setStatus('current')
if mibBuilder.loadTexts: cvUriClassSIPUserIDPreference.setDescription('Preference assigned to the match length resulting from a match of cvSIPUriClassCfgUserIDPattern against the user-id portion of a sip: URI.')
cvUriClassMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2))
cvUriClassMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1))
cvUriClassMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2))
cvUriClassMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1, 1)).setObjects(("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvUriClassMIBCompliance = cvUriClassMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvUriClassMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO VOICE URI CLASS MIB.')
cvUriClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2, 1)).setObjects(("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgType"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgStatus"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgUserIDPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgHostPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgPhoneCtxtPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneNumPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneCtxtPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvCommonUriClassCfgURIPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPHostPreference"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPUserIDPreference"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvUriClassGroup = cvUriClassGroup.setStatus('current')
if mibBuilder.loadTexts: cvUriClassGroup.setDescription('A collection of objects providing the general Voice URI Class configuration capability.')
mibBuilder.exportSymbols("CISCO-VOICE-URI-CLASS-MIB", cvSIPUriClassCfgUserIDPattern=cvSIPUriClassCfgUserIDPattern, cvUriClassSIPGeneralConfig=cvUriClassSIPGeneralConfig, cvTELUriClassCfgPhoneCtxtPattern=cvTELUriClassCfgPhoneCtxtPattern, CvUriClassTag=CvUriClassTag, cvUriClassCfgTable=cvUriClassCfgTable, cvUriClassCfgTag=cvUriClassCfgTag, cvUriClassCfgEntry=cvUriClassCfgEntry, cvTELUriClassCfgPhoneNumPattern=cvTELUriClassCfgPhoneNumPattern, cvUriClassMIBNotifications=cvUriClassMIBNotifications, ciscoVoiceUriClassMIB=ciscoVoiceUriClassMIB, cvSIPUriClassCfgTable=cvSIPUriClassCfgTable, cvUriClass=cvUriClass, cvTELUriClassCfgTable=cvTELUriClassCfgTable, cvUriClassCfgType=cvUriClassCfgType, cvUriClassMIBCompliances=cvUriClassMIBCompliances, cvCommonUriClassCfgTable=cvCommonUriClassCfgTable, cvUriClassSIPHostPreference=cvUriClassSIPHostPreference, cvSIPUriClassCfgPhoneCtxtPattern=cvSIPUriClassCfgPhoneCtxtPattern, cvUriClassMIBGroups=cvUriClassMIBGroups, PYSNMP_MODULE_ID=ciscoVoiceUriClassMIB, cvUriClassMIBObjects=cvUriClassMIBObjects, cvCommonUriClassCfgURIPattern=cvCommonUriClassCfgURIPattern, cvUriClassGroup=cvUriClassGroup, cvUriClassCfgStatus=cvUriClassCfgStatus, cvUriClassMIBConformance=cvUriClassMIBConformance, cvUriClassSIPUserIDPreference=cvUriClassSIPUserIDPreference, cvUriClassMIBCompliance=cvUriClassMIBCompliance, CvUriClassTagIndex=CvUriClassTagIndex, cvCommonUriClassCfgEntry=cvCommonUriClassCfgEntry, CvUriClassPreference=CvUriClassPreference, cvSIPUriClassCfgEntry=cvSIPUriClassCfgEntry, cvTELUriClassCfgEntry=cvTELUriClassCfgEntry, CvUriClassPattern=CvUriClassPattern, cvSIPUriClassCfgHostPattern=cvSIPUriClassCfgHostPattern)
