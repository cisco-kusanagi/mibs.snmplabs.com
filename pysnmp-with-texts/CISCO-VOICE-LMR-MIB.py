#
# PySNMP MIB module CISCO-VOICE-LMR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-LMR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, Integer32, MibIdentifier, Counter32, ObjectIdentity, Gauge32, Counter64, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibIdentifier", "Counter32", "ObjectIdentity", "Gauge32", "Counter64", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "iso", "Unsigned32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoVoiceLmrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 510))
ciscoVoiceLmrMIB.setRevisions(('2004-10-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setRevisionsDescriptions(('the initial version of the MIB.',))
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setLastUpdated('200410140000Z')
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setDescription('This MIB module provides management of voice tone signal as static injected tone for Land Mobile Radio The tone signal includes tone, pause, guard/idle tone. User can configure a sequence of tone and pause to be played out before any voice sample is played out. These tones are used to wake up the radio and select the radio channel. During the voice playout, a configured guard tone will be mixed with the voice to keep the radio active. For some radio systems, there is no need for the guard tone, but a configured idle tone is needed to inform the radio that the channel is idle. It is possible that the radio system will generate guard/idle tone. In that case, the IOS can instruct the DSP to filter out the radio generated guard/idle tone by enabling digital filter. Digital filter is able to filter out either 1950HZ or 2175HZ tone. ')
cvlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 1))
cvlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2))
cvlToneObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1))
class VoiceFrequency(TextualConvention, Unsigned32):
    description = 'This textual convention is used to represent the audible voice frequency between 1HZ to 4000HZ. Value 0 indicates this textual convention is not configured. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4000)

class VoiceAmplitude(TextualConvention, Integer32):
    description = 'This textual convention is used to represent the amplitude of voice between -30 to 3 dbm. dbm is the absolute output and input optical power levels in mW. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-30, 3)

class LmrToneDuration(TextualConvention, Unsigned32):
    description = 'This textual convention is used to represent the duration of tone played. It is measured in milliseconds. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 500)

cvlClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1), )
if mibBuilder.loadTexts: cvlClassTable.setStatus('current')
if mibBuilder.loadTexts: cvlClassTable.setDescription('The table contains the LMR guard/idle tone frequency and amplitude. It also specifies what frequency will be filtered out from radio voice input by dsp digital filter. ')
cvlClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VOICE-LMR-MIB", "cvlClassIndex"))
if mibBuilder.loadTexts: cvlClassEntry.setStatus('current')
if mibBuilder.loadTexts: cvlClassEntry.setDescription('A concept row in cvlClassTable. It has class name, tone frequency, tone amplitude, guard/idle tone indicator and digital filter information. ')
cvlClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)))
if mibBuilder.loadTexts: cvlClassIndex.setStatus('current')
if mibBuilder.loadTexts: cvlClassIndex.setDescription('An arbitrary integer which increases monotonically to index the cvlClassTable. ')
cvlClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlClassName.setStatus('current')
if mibBuilder.loadTexts: cvlClassName.setDescription('The object reflects the voice class name.')
cvlDigitalFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("digitalFilterNone", 0), ("digitalFilter1950HZ", 1), ("digitalFilter2175HZ", 2))).clone('digitalFilterNone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlDigitalFilter.setStatus('current')
if mibBuilder.loadTexts: cvlDigitalFilter.setDescription('This object reflects which tone frequency should be filtered out from radio input. ')
cvlGuardToneFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 4), VoiceFrequency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlGuardToneFreq.setStatus('current')
if mibBuilder.loadTexts: cvlGuardToneFreq.setDescription('This object reflects the guard/idle tone frequency between 1-4000 HZ. If there is no guard/idle tone configured for this voice class, cvlGuardToneFreq has value 0. ')
cvlGuardToneAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 5), VoiceAmplitude()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlGuardToneAmp.setStatus('current')
if mibBuilder.loadTexts: cvlGuardToneAmp.setDescription('This object reflects the guard/idle tone amplitude in dbm. ')
cvlIdleToneFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlIdleToneFlag.setStatus('current')
if mibBuilder.loadTexts: cvlIdleToneFlag.setDescription('This object reflects this voice class has guard/idle tone configured. true means guard tone and false means idle tone. ')
cvlSignalToneTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2), )
if mibBuilder.loadTexts: cvlSignalToneTable.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneTable.setDescription('The table contains the LMR injected tone information and playout sequence for voice class tone signal. The tones with same cvlSignalToneGroupIndex will be played out in ascending order of the cvlSignalToneIndex. ')
cvlSignalToneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VOICE-LMR-MIB", "cvlSignalToneGroupIndex"), (0, "CISCO-VOICE-LMR-MIB", "cvlSignalToneIndex"))
if mibBuilder.loadTexts: cvlSignalToneEntry.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneEntry.setDescription('An entry in the table, containing information about a single tone.')
cvlSignalToneGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)))
if mibBuilder.loadTexts: cvlSignalToneGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneGroupIndex.setDescription('This object reflects a group of tones. The tones with same cvlSignalToneGroupIndex will be played out in ascending order of the cvlSignalToneIndex. ')
cvlSignalToneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)))
if mibBuilder.loadTexts: cvlSignalToneIndex.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneIndex.setDescription('This object reflects the tone playout sequence in ascending order of the index for the tones with same cvlSignalToneGroupIndex value. ')
cvlSignalToneName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneName.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneName.setDescription('The object reflects the tone signal class name.')
cvlSignalToneFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 4), VoiceFrequency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneFreq.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneFreq.setDescription('This object reflects the tone frequency in HZ. If the value is 0 then no tone will be played out and can be used to provide pause during a sequence of tones. ')
cvlSignalToneAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 5), VoiceAmplitude()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneAmp.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneAmp.setDescription('This object reflects the signal tone amplitude in dbm.')
cvlSignalToneDur = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 6), LmrToneDuration()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneDur.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneDur.setDescription('This object reflects the signal tone duration.')
cvlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1))
cvlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2))
cvlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1, 1)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlToneClassGroup"), ("CISCO-VOICE-LMR-MIB", "cvlToneSignalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlMIBCompliance = cvlMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvlMIBCompliance.setDescription('The compliance statements for the Cisco Land Mobile Radio (LMR) MIB. ')
cvlToneClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 1)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlClassName"), ("CISCO-VOICE-LMR-MIB", "cvlDigitalFilter"), ("CISCO-VOICE-LMR-MIB", "cvlGuardToneFreq"), ("CISCO-VOICE-LMR-MIB", "cvlGuardToneAmp"), ("CISCO-VOICE-LMR-MIB", "cvlIdleToneFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlToneClassGroup = cvlToneClassGroup.setStatus('current')
if mibBuilder.loadTexts: cvlToneClassGroup.setDescription('A collection of objects that provide info applicable to digital notch filter or guard/idle tone. ')
cvlToneSignalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 2)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlSignalToneName"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneFreq"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneAmp"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneDur"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlToneSignalGroup = cvlToneSignalGroup.setStatus('current')
if mibBuilder.loadTexts: cvlToneSignalGroup.setDescription('A collection of objects that provide info applicable to either wake-up tone, function selection or pause between tones. It also provides the info about the playout sequence of the tones. ')
mibBuilder.exportSymbols("CISCO-VOICE-LMR-MIB", LmrToneDuration=LmrToneDuration, cvlToneClassGroup=cvlToneClassGroup, cvlSignalToneDur=cvlSignalToneDur, cvlSignalToneName=cvlSignalToneName, ciscoVoiceLmrMIB=ciscoVoiceLmrMIB, cvlSignalToneIndex=cvlSignalToneIndex, cvlMIBConformance=cvlMIBConformance, cvlClassTable=cvlClassTable, cvlIdleToneFlag=cvlIdleToneFlag, cvlSignalToneFreq=cvlSignalToneFreq, cvlSignalToneTable=cvlSignalToneTable, cvlSignalToneAmp=cvlSignalToneAmp, cvlMIBObjects=cvlMIBObjects, cvlGuardToneFreq=cvlGuardToneFreq, cvlToneSignalGroup=cvlToneSignalGroup, cvlToneObjects=cvlToneObjects, cvlClassName=cvlClassName, VoiceFrequency=VoiceFrequency, cvlSignalToneGroupIndex=cvlSignalToneGroupIndex, PYSNMP_MODULE_ID=ciscoVoiceLmrMIB, cvlGuardToneAmp=cvlGuardToneAmp, cvlMIBCompliances=cvlMIBCompliances, cvlClassIndex=cvlClassIndex, cvlSignalToneEntry=cvlSignalToneEntry, VoiceAmplitude=VoiceAmplitude, cvlMIBCompliance=cvlMIBCompliance, cvlDigitalFilter=cvlDigitalFilter, cvlClassEntry=cvlClassEntry, cvlMIBGroups=cvlMIBGroups)
