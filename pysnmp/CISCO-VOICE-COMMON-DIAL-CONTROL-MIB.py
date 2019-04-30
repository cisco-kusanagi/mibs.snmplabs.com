#
# PySNMP MIB module CISCO-VOICE-COMMON-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-COMMON-DIAL-CONTROL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
callActiveIndex, callActiveSetupTime = mibBuilder.importSymbols("DIAL-CONTROL-MIB", "callActiveIndex", "callActiveSetupTime")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ModuleIdentity, NotificationType, Integer32, Counter32, ObjectIdentity, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ModuleIdentity", "NotificationType", "Integer32", "Counter32", "ObjectIdentity", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoVoiceCommonDialControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 55))
ciscoVoiceCommonDialControlMIB.setRevisions(('2010-06-30 00:00', '2009-03-18 00:00', '2008-07-02 00:00', '2007-06-26 00:00', '2005-08-16 00:00', '2005-03-06 00:00', '2003-03-11 00:00', '2001-10-06 00:00', '2001-09-05 00:00', '2000-07-22 00:00',))
if mibBuilder.loadTexts: ciscoVoiceCommonDialControlMIB.setLastUpdated('201006300000Z')
if mibBuilder.loadTexts: ciscoVoiceCommonDialControlMIB.setOrganization('Cisco Systems, Inc.')
cvCommonDcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 1))
cvCommonDcCallActive = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1))
cvCommonDcCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2))
class CvcSpeechCoderRate(TextualConvention, Integer32):
    reference = '[1] RFC 3267: For introduction about GSM AMR-NB codec, section 3.1 [2] RFC 3952: For introduction about iLBC codec, section 2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30))
    namedValues = NamedValues(("g729r8000", 1), ("g729Ar8000", 2), ("g726r16000", 3), ("g726r24000", 4), ("g726r32000", 5), ("g711ulawr64000", 6), ("g711Alawr64000", 7), ("g728r16000", 8), ("g723r6300", 9), ("g723r5300", 10), ("gsmr13200", 11), ("g729Br8000", 12), ("g729ABr8000", 13), ("g723Ar6300", 14), ("g723Ar5300", 15), ("g729IETFr8000", 16), ("gsmeEr12200", 17), ("clearChannel", 18), ("g726r40000", 19), ("llcc", 20), ("gsmAmrNb", 21), ("iLBC", 22), ("iLBCr15200", 23), ("iLBCr13330", 24), ("g722r4800", 25), ("g722r5600", 26), ("g722r6400", 27), ("iSAC", 28), ("aaclc", 29), ("aacld", 30))

class CvcFaxTransmitRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("none", 1), ("voiceRate", 2), ("fax2400", 3), ("fax4800", 4), ("fax7200", 5), ("fax9600", 6), ("fax14400", 7), ("fax12000", 8))

class CvcCoderTypeRate(TextualConvention, Integer32):
    reference = '[1] RFC 3267: For introduction about GSM AMR-NB codec, section 3.1 [2] RFC 3952: For introduction about iLBC codec, section 2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))
    namedValues = NamedValues(("other", 1), ("fax2400", 2), ("fax4800", 3), ("fax7200", 4), ("fax9600", 5), ("fax14400", 6), ("fax12000", 7), ("g729r8000", 10), ("g729Ar8000", 11), ("g726r16000", 12), ("g726r24000", 13), ("g726r32000", 14), ("g711ulawr64000", 15), ("g711Alawr64000", 16), ("g728r16000", 17), ("g723r6300", 18), ("g723r5300", 19), ("gsmr13200", 20), ("g729Br8000", 21), ("g729ABr8000", 22), ("g723Ar6300", 23), ("g723Ar5300", 24), ("ietfg729r8000", 25), ("gsmeEr12200", 26), ("clearChannel", 27), ("g726r40000", 28), ("llcc", 29), ("gsmAmrNb", 30), ("g722", 31), ("iLBC", 32), ("iLBCr15200", 33), ("iLBCr13330", 34), ("g722r4800", 35), ("g722r5600", 36), ("g722r6400", 37), ("iSAC", 38), ("aaclc", 39), ("aacld", 40))

class CvcGUid(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class CvcInBandSignaling(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("cas", 1), ("none", 2), ("cept", 3), ("transparent", 4), ("gr303", 5))

class CvcCallReferenceIdOrZero(TextualConvention, Unsigned32):
    status = 'current'

class CvcH320CallType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("primary", 1), ("secondary", 2))

class CvcVideoCoderRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("h261", 1), ("h263", 2), ("h263plus", 3), ("h264", 4))

cvCommonDcCallActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1), )
if mibBuilder.loadTexts: cvCommonDcCallActiveTable.setStatus('current')
cvCommonDcCallActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1), ).setIndexNames((0, "DIAL-CONTROL-MIB", "callActiveSetupTime"), (0, "DIAL-CONTROL-MIB", "callActiveIndex"))
if mibBuilder.loadTexts: cvCommonDcCallActiveEntry.setStatus('current')
cvCommonDcCallActiveConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveConnectionId.setStatus('current')
cvCommonDcCallActiveVADEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveVADEnable.setStatus('current')
cvCommonDcCallActiveCoderTypeRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 3), CvcCoderTypeRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveCoderTypeRate.setStatus('current')
cvCommonDcCallActiveCodecBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveCodecBytes.setStatus('current')
cvCommonDcCallActiveInBandSignaling = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 5), CvcInBandSignaling()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveInBandSignaling.setStatus('current')
cvCommonDcCallActiveCallingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveCallingName.setStatus('current')
cvCommonDcCallActiveCallerIDBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 1, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallActiveCallerIDBlock.setStatus('current')
cvCommonDcCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1), )
if mibBuilder.loadTexts: cvCommonDcCallHistoryTable.setStatus('current')
cvCommonDcCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cvCommonDcCallHistoryEntry.setStatus('current')
cvCommonDcCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryConnectionId.setStatus('current')
cvCommonDcCallHistoryVADEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryVADEnable.setStatus('current')
cvCommonDcCallHistoryCoderTypeRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 3), CvcCoderTypeRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryCoderTypeRate.setStatus('current')
cvCommonDcCallHistoryCodecBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryCodecBytes.setStatus('current')
cvCommonDcCallHistoryInBandSignaling = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 5), CvcInBandSignaling()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryInBandSignaling.setStatus('current')
cvCommonDcCallHistoryCallingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryCallingName.setStatus('current')
cvCommonDcCallHistoryCallerIDBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 55, 1, 2, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvCommonDcCallHistoryCallerIDBlock.setStatus('current')
cvCommonDcMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 2))
cvCommonDcMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 2, 0))
cvCommonDcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 3))
cvCommonDcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 1))
cvCommonDcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 2))
cvCommonDcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 1, 1)).setObjects(("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvCommonDcMIBCompliance = cvCommonDcMIBCompliance.setStatus('deprecated')
cvCommonDcMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 1, 2)).setObjects(("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvCommonDcMIBComplianceRev1 = cvCommonDcMIBComplianceRev1.setStatus('current')
cvCommonDcCallGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 2, 1)).setObjects(("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveConnectionId"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveVADEnable"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCoderTypeRate"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCodecBytes"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveInBandSignaling"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryConnectionId"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryVADEnable"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCoderTypeRate"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCodecBytes"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryInBandSignaling"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvCommonDcCallGroup = cvCommonDcCallGroup.setStatus('deprecated')
cvCommonDcCallGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 55, 3, 2, 2)).setObjects(("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveConnectionId"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveVADEnable"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCoderTypeRate"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCodecBytes"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveInBandSignaling"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCallingName"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallActiveCallerIDBlock"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryConnectionId"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryVADEnable"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCoderTypeRate"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCodecBytes"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryInBandSignaling"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCallingName"), ("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "cvCommonDcCallHistoryCallerIDBlock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvCommonDcCallGroup1 = cvCommonDcCallGroup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", cvCommonDcMIBGroups=cvCommonDcMIBGroups, CvcGUid=CvcGUid, ciscoVoiceCommonDialControlMIB=ciscoVoiceCommonDialControlMIB, cvCommonDcCallActiveVADEnable=cvCommonDcCallActiveVADEnable, cvCommonDcCallActive=cvCommonDcCallActive, cvCommonDcCallGroup=cvCommonDcCallGroup, cvCommonDcCallActiveCallerIDBlock=cvCommonDcCallActiveCallerIDBlock, cvCommonDcMIBConformance=cvCommonDcMIBConformance, CvcCallReferenceIdOrZero=CvcCallReferenceIdOrZero, cvCommonDcCallActiveCallingName=cvCommonDcCallActiveCallingName, cvCommonDcCallActiveInBandSignaling=cvCommonDcCallActiveInBandSignaling, cvCommonDcMIBCompliances=cvCommonDcMIBCompliances, cvCommonDcCallActiveEntry=cvCommonDcCallActiveEntry, cvCommonDcCallHistoryCallingName=cvCommonDcCallHistoryCallingName, CvcSpeechCoderRate=CvcSpeechCoderRate, cvCommonDcCallActiveCodecBytes=cvCommonDcCallActiveCodecBytes, CvcInBandSignaling=CvcInBandSignaling, cvCommonDcMIBCompliance=cvCommonDcMIBCompliance, PYSNMP_MODULE_ID=ciscoVoiceCommonDialControlMIB, cvCommonDcCallHistoryInBandSignaling=cvCommonDcCallHistoryInBandSignaling, cvCommonDcCallHistoryCallerIDBlock=cvCommonDcCallHistoryCallerIDBlock, cvCommonDcCallActiveConnectionId=cvCommonDcCallActiveConnectionId, cvCommonDcCallHistoryVADEnable=cvCommonDcCallHistoryVADEnable, CvcVideoCoderRate=CvcVideoCoderRate, CvcCoderTypeRate=CvcCoderTypeRate, cvCommonDcCallHistoryConnectionId=cvCommonDcCallHistoryConnectionId, cvCommonDcMIBNotifications=cvCommonDcMIBNotifications, cvCommonDcCallHistory=cvCommonDcCallHistory, CvcFaxTransmitRate=CvcFaxTransmitRate, cvCommonDcCallActiveTable=cvCommonDcCallActiveTable, cvCommonDcCallActiveCoderTypeRate=cvCommonDcCallActiveCoderTypeRate, cvCommonDcCallHistoryEntry=cvCommonDcCallHistoryEntry, cvCommonDcCallHistoryCoderTypeRate=cvCommonDcCallHistoryCoderTypeRate, cvCommonDcMIBComplianceRev1=cvCommonDcMIBComplianceRev1, cvCommonDcMIBNotificationPrefix=cvCommonDcMIBNotificationPrefix, CvcH320CallType=CvcH320CallType, cvCommonDcCallHistoryCodecBytes=cvCommonDcCallHistoryCodecBytes, cvCommonDcCallHistoryTable=cvCommonDcCallHistoryTable, cvCommonDcMIBObjects=cvCommonDcMIBObjects, cvCommonDcCallGroup1=cvCommonDcCallGroup1)
