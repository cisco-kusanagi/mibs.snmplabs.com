#
# PySNMP MIB module CISCO-VOICE-URI-CLASS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-URI-CLASS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, Gauge32, Unsigned32, iso, IpAddress, TimeTicks, Counter32, Counter64, ObjectIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "Unsigned32", "iso", "IpAddress", "TimeTicks", "Counter32", "Counter64", "ObjectIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoVoiceUriClassMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 99999999))
ciscoVoiceUriClassMIB.setRevisions(('2002-10-10 00:00',))
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setLastUpdated('200210100000Z')
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setOrganization('Cisco Systems, Inc.')
class CvUriClassTagIndex(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class CvUriClassTag(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvUriClassPattern(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvUriClassPreference(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 10)

cvUriClassMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 0))
cvUriClassMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1))
cvUriClass = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1))
cvUriClassSIPGeneralConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2))
cvUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1), )
if mibBuilder.loadTexts: cvUriClassCfgTable.setStatus('current')
cvUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvUriClassCfgEntry.setStatus('current')
cvUriClassCfgTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 1), CvUriClassTagIndex())
if mibBuilder.loadTexts: cvUriClassCfgTag.setStatus('current')
cvUriClassCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sip", 1), ("tel", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvUriClassCfgType.setStatus('current')
cvUriClassCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvUriClassCfgStatus.setStatus('current')
cvSIPUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2), )
if mibBuilder.loadTexts: cvSIPUriClassCfgTable.setStatus('current')
cvSIPUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvSIPUriClassCfgEntry.setStatus('current')
cvSIPUriClassCfgUserIDPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 1), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgUserIDPattern.setStatus('current')
cvSIPUriClassCfgHostPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 2), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgHostPattern.setStatus('current')
cvSIPUriClassCfgPhoneCtxtPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 3), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgPhoneCtxtPattern.setStatus('current')
cvTELUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3), )
if mibBuilder.loadTexts: cvTELUriClassCfgTable.setStatus('current')
cvTELUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvTELUriClassCfgEntry.setStatus('current')
cvTELUriClassCfgPhoneNumPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 1), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneNumPattern.setStatus('current')
cvTELUriClassCfgPhoneCtxtPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 2), CvUriClassPattern()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneCtxtPattern.setStatus('current')
cvCommonUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4), )
if mibBuilder.loadTexts: cvCommonUriClassCfgTable.setStatus('current')
cvCommonUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1), ).setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvCommonUriClassCfgEntry.setStatus('current')
cvCommonUriClassCfgURIPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvCommonUriClassCfgURIPattern.setStatus('current')
cvUriClassSIPHostPreference = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 1), CvUriClassPreference().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvUriClassSIPHostPreference.setStatus('current')
cvUriClassSIPUserIDPreference = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 2), CvUriClassPreference().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvUriClassSIPUserIDPreference.setStatus('current')
cvUriClassMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2))
cvUriClassMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1))
cvUriClassMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2))
cvUriClassMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1, 1)).setObjects(("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvUriClassMIBCompliance = cvUriClassMIBCompliance.setStatus('current')
cvUriClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2, 1)).setObjects(("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgType"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgStatus"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgUserIDPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgHostPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgPhoneCtxtPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneNumPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneCtxtPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvCommonUriClassCfgURIPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPHostPreference"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPUserIDPreference"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvUriClassGroup = cvUriClassGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-URI-CLASS-MIB", cvUriClassCfgEntry=cvUriClassCfgEntry, cvTELUriClassCfgTable=cvTELUriClassCfgTable, cvSIPUriClassCfgEntry=cvSIPUriClassCfgEntry, cvSIPUriClassCfgTable=cvSIPUriClassCfgTable, cvUriClassMIBCompliances=cvUriClassMIBCompliances, cvTELUriClassCfgPhoneNumPattern=cvTELUriClassCfgPhoneNumPattern, cvTELUriClassCfgEntry=cvTELUriClassCfgEntry, CvUriClassPreference=CvUriClassPreference, cvTELUriClassCfgPhoneCtxtPattern=cvTELUriClassCfgPhoneCtxtPattern, cvUriClassMIBGroups=cvUriClassMIBGroups, cvSIPUriClassCfgUserIDPattern=cvSIPUriClassCfgUserIDPattern, cvUriClassCfgType=cvUriClassCfgType, cvCommonUriClassCfgEntry=cvCommonUriClassCfgEntry, cvCommonUriClassCfgURIPattern=cvCommonUriClassCfgURIPattern, cvUriClassMIBCompliance=cvUriClassMIBCompliance, cvUriClassCfgTable=cvUriClassCfgTable, cvUriClassMIBNotifications=cvUriClassMIBNotifications, CvUriClassTag=CvUriClassTag, cvSIPUriClassCfgPhoneCtxtPattern=cvSIPUriClassCfgPhoneCtxtPattern, CvUriClassPattern=CvUriClassPattern, PYSNMP_MODULE_ID=ciscoVoiceUriClassMIB, cvUriClassSIPUserIDPreference=cvUriClassSIPUserIDPreference, cvSIPUriClassCfgHostPattern=cvSIPUriClassCfgHostPattern, cvUriClassSIPHostPreference=cvUriClassSIPHostPreference, cvUriClassCfgTag=cvUriClassCfgTag, cvUriClassMIBObjects=cvUriClassMIBObjects, cvUriClassMIBConformance=cvUriClassMIBConformance, ciscoVoiceUriClassMIB=ciscoVoiceUriClassMIB, cvUriClassCfgStatus=cvUriClassCfgStatus, CvUriClassTagIndex=CvUriClassTagIndex, cvUriClassSIPGeneralConfig=cvUriClassSIPGeneralConfig, cvUriClass=cvUriClass, cvCommonUriClassCfgTable=cvCommonUriClassCfgTable, cvUriClassGroup=cvUriClassGroup)
