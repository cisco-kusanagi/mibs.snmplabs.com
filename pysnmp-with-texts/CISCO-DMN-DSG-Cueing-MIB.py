#
# PySNMP MIB module CISCO-DMN-DSG-Cueing-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-Cueing-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:54:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, MibIdentifier, Bits, Counter32, NotificationType, TimeTicks, Gauge32, Unsigned32, ObjectIdentity, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "MibIdentifier", "Bits", "Counter32", "NotificationType", "TimeTicks", "Gauge32", "Unsigned32", "ObjectIdentity", "Counter64", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGCueing = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33))
ciscoDSGCueing.setRevisions(('2010-08-30 08:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGCueing.setRevisionsDescriptions(('V01.00.00 2010-08-30 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGCueing.setLastUpdated('201008300800Z')
if mibBuilder.loadTexts: ciscoDSGCueing.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGCueing.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGCueing.setDescription('Cisco Cueing MIB.')
cueingTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11))
cueingMode = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("trigger", 1), ("tone", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingMode.setStatus('current')
if mibBuilder.loadTexts: cueingMode.setDescription('Selection of Cueing Mode.')
cueingTrigPol = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingTrigPol.setStatus('current')
if mibBuilder.loadTexts: cueingTrigPol.setDescription('Selection of Cueing Trigger Polarity.')
cueingRepeatCnt = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingRepeatCnt.setStatus('current')
if mibBuilder.loadTexts: cueingRepeatCnt.setDescription('Cueing Tone repeat count.')
cueingTone = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingTone.setStatus('current')
if mibBuilder.loadTexts: cueingTone.setDescription('Cueing Tone duration in milliseconds.')
cueingSilence = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingSilence.setStatus('current')
if mibBuilder.loadTexts: cueingSilence.setDescription('Silence duration in milliseconds.')
cueingRelayMode = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("alarm", 1), ("trigger", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingRelayMode.setStatus('current')
if mibBuilder.loadTexts: cueingRelayMode.setDescription('Selection of Relay Mode.')
cueingRelayTrigBit = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingRelayTrigBit.setStatus('current')
if mibBuilder.loadTexts: cueingRelayTrigBit.setDescription('Selection of Relay trigger bit.')
cueingTestToneSequence = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingTestToneSequence.setStatus('current')
if mibBuilder.loadTexts: cueingTestToneSequence.setDescription('Cueing test tone sequence.')
cueingTestToneStartStop = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingTestToneStartStop.setStatus('current')
if mibBuilder.loadTexts: cueingTestToneStartStop.setDescription('Cueing test tone start/stop.')
cueingTestToneGo = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingTestToneGo.setStatus('current')
if mibBuilder.loadTexts: cueingTestToneGo.setDescription('Cueing test tone go.')
cueingToneSeqTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1), )
if mibBuilder.loadTexts: cueingToneSeqTable.setStatus('current')
if mibBuilder.loadTexts: cueingToneSeqTable.setDescription('Cueing Tone sequence Table.')
cueingToneSeqEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-Cueing-MIB", "cueingToneSeqNum"))
if mibBuilder.loadTexts: cueingToneSeqEntry.setStatus('current')
if mibBuilder.loadTexts: cueingToneSeqEntry.setDescription('Entry for Cueing tone table.')
cueingToneSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: cueingToneSeqNum.setStatus('current')
if mibBuilder.loadTexts: cueingToneSeqNum.setDescription('Cueing Tone sequence number selection.')
cueingToneSeqState = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingToneSeqState.setStatus('current')
if mibBuilder.loadTexts: cueingToneSeqState.setDescription('Contact Tone Sequence state selection.')
cueingToneSeqTones = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingToneSeqTones.setStatus('current')
if mibBuilder.loadTexts: cueingToneSeqTones.setDescription('Cueing Tone sequence tones.')
cueingToneSeqMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("start", 1), ("stop", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingToneSeqMode.setStatus('current')
if mibBuilder.loadTexts: cueingToneSeqMode.setDescription('Contact Tone Sequence mode selection.')
cueingToneSeqDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueingToneSeqDelay.setStatus('current')
if mibBuilder.loadTexts: cueingToneSeqDelay.setDescription('Cueing Tone sequence delay in seconds.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-Cueing-MIB", cueingTrigPol=cueingTrigPol, cueingToneSeqState=cueingToneSeqState, cueingTestToneGo=cueingTestToneGo, PYSNMP_MODULE_ID=ciscoDSGCueing, cueingTestToneStartStop=cueingTestToneStartStop, cueingToneSeqEntry=cueingToneSeqEntry, cueingToneSeqNum=cueingToneSeqNum, cueingToneSeqTones=cueingToneSeqTones, cueingToneSeqDelay=cueingToneSeqDelay, cueingMode=cueingMode, cueingRelayTrigBit=cueingRelayTrigBit, cueingToneSeqTable=cueingToneSeqTable, cueingTable=cueingTable, cueingRelayMode=cueingRelayMode, ciscoDSGCueing=ciscoDSGCueing, cueingToneSeqMode=cueingToneSeqMode, cueingTestToneSequence=cueingTestToneSequence, cueingSilence=cueingSilence, cueingRepeatCnt=cueingRepeatCnt, cueingTone=cueingTone)
