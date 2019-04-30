#
# PySNMP MIB module TPT-HIGH-AVAIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-HIGH-AVAIL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, MibIdentifier, ModuleIdentity, Unsigned32, Bits, Counter64, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits", "Counter64", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
EnabledOrNot, = mibBuilder.importSymbols("TPT-PORT-CONFIG-MIB", "EnabledOrNot")
tpt_tpa_objs, tpt_tpa_unkparams, tpt_tpa_eventsV2 = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs", "tpt-tpa-unkparams", "tpt-tpa-eventsV2")
tpt_high_avail_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6)).setLabel("tpt-high-avail-objs")
tpt_high_avail_objs.setRevisions(('2016-09-08 18:54', '2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_high_avail_objs.setLastUpdated('201609081854Z')
if mibBuilder.loadTexts: tpt_high_avail_objs.setOrganization('Trend Micro, Inc.')
class FaultState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("normal", 0), ("fallback", 1))

class FaultCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("none", 0), ("suspended-task", 1), ("out-of-memory", 2), ("hardware-breakpoint", 3), ("tse-failure", 4), ("watchdog-timeout", 5), ("user-reset", 6), ("user-fallback", 7), ("threshold-failure", 8), ("software-watchdog-timeout", 9), ("oam-fault", 10), ("hard-disk-disable", 11), ("initialization-failure", 12), ("internal-link-failure", 13), ("multiple-fan-failures", 14), ("packet-egress-integrity", 15), ("stack-master", 16), ("waiting-on-stack", 17), ("spike-reboot-or-halt", 18), ("process-error", 19), ("low-health-score", 20))

class ConnectionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-connected", 0), ("unresponsive", 1), ("connected", 2))

class PerfProtPhase(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("entering", 1), ("continuing", 2), ("exiting", 3))

class ZphaState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("normal", 0), ("ips-bypass", 1))

class ZphaAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("normal", 1), ("bypass", 2))

class ZphaMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("single", 2), ("multi", 3))

class ZphaPresent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("absent", 0), ("present", 1))

highAvailTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailTimeStamp.setStatus('current')
highAvailFaultState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 2), FaultState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailFaultState.setStatus('current')
highAvailFaultCause = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 3), FaultCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailFaultCause.setStatus('current')
highAvailThresholdEnabled = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 4), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailThresholdEnabled.setStatus('current')
highAvailThresholdPercent = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailThresholdPercent.setStatus('current')
highAvailEnabled = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 6), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailEnabled.setStatus('current')
highAvailTransparentState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 7), ConnectionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailTransparentState.setStatus('current')
highAvailTransparentEnabled = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 8), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailTransparentEnabled.setStatus('current')
highAvailTransparentPartner = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailTransparentPartner.setStatus('current')
highAvailZeroPowerState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 10), ZphaState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerState.setStatus('current')
highAvailZeroPowerQuantity = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerQuantity.setStatus('current')
highAvailZeroPowerTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12), )
if mibBuilder.loadTexts: highAvailZeroPowerTable.setStatus('current')
highAvailZeroPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1), ).setIndexNames((0, "TPT-HIGH-AVAIL-MIB", "highAvailZeroPowerIndex"))
if mibBuilder.loadTexts: highAvailZeroPowerEntry.setStatus('current')
highAvailZeroPowerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 1), Unsigned32())
if mibBuilder.loadTexts: highAvailZeroPowerIndex.setStatus('current')
highAvailZeroPowerSegment = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerSegment.setStatus('current')
highAvailZeroPowerActive = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 3), ZphaState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerActive.setStatus('current')
highAvailZeroPowerAction = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 4), ZphaAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerAction.setStatus('current')
highAvailZeroPowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 5), ZphaMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerMode.setStatus('current')
highAvailZeroPowerPresence = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 13), ZphaPresent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerPresence.setStatus('current')
tptIhaNotifyDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 81), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptIhaNotifyDeviceID.setStatus('current')
tptIhaNotifyTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 82), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptIhaNotifyTimeStamp.setStatus('current')
tptIhaNotifyFaultState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 83), FaultState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptIhaNotifyFaultState.setStatus('current')
tptIhaNotifyFaultCause = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 84), FaultCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptIhaNotifyFaultCause.setStatus('current')
tptIhaNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 15)).setObjects(("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyDeviceID"), ("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyTimeStamp"), ("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyFaultState"), ("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyFaultCause"))
if mibBuilder.loadTexts: tptIhaNotify.setStatus('current')
tptTrhaNotifyDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 86), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTrhaNotifyDeviceID.setStatus('current')
tptTrhaNotifyTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 87), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTrhaNotifyTimeStamp.setStatus('current')
tptTrhaNotifyNewState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 88), ConnectionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTrhaNotifyNewState.setStatus('current')
tptTrhaNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 18)).setObjects(("TPT-HIGH-AVAIL-MIB", "tptTrhaNotifyDeviceID"), ("TPT-HIGH-AVAIL-MIB", "tptTrhaNotifyTimeStamp"), ("TPT-HIGH-AVAIL-MIB", "tptTrhaNotifyNewState"))
if mibBuilder.loadTexts: tptTrhaNotify.setStatus('current')
tptZphaNotifyDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 161), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptZphaNotifyDeviceID.setStatus('current')
tptZphaNotifyTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 162), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptZphaNotifyTimeStamp.setStatus('current')
tptZphaNotifySegmentName = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 163), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptZphaNotifySegmentName.setStatus('current')
tptZphaNotifyNewState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 164), ZphaState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptZphaNotifyNewState.setStatus('current')
tptZphaNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 24)).setObjects(("TPT-HIGH-AVAIL-MIB", "tptZphaNotifyDeviceID"), ("TPT-HIGH-AVAIL-MIB", "tptZphaNotifyTimeStamp"), ("TPT-HIGH-AVAIL-MIB", "tptZphaNotifySegmentName"), ("TPT-HIGH-AVAIL-MIB", "tptZphaNotifyNewState"))
if mibBuilder.loadTexts: tptZphaNotify.setStatus('current')
tptPerfProtNotifyDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 141), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyDeviceID.setStatus('current')
tptPerfProtNotifyTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 142), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyTimeStamp.setStatus('current')
tptPerfProtNotifyPhase = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 143), PerfProtPhase()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyPhase.setStatus('current')
tptPerfProtNotifyPacketLoss = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 144), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyPacketLoss.setStatus('current')
tptPerfProtNotifyLossThreshold = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 145), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyLossThreshold.setStatus('current')
tptPerfProtNotifyDuration = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 146), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyDuration.setStatus('current')
tptPerfProtNotifyMissedAlerts = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 147), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyMissedAlerts.setStatus('current')
tptPerfProtNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 21)).setObjects(("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyDeviceID"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyTimeStamp"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyPhase"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyPacketLoss"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyLossThreshold"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyDuration"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyMissedAlerts"))
if mibBuilder.loadTexts: tptPerfProtNotify.setStatus('current')
mibBuilder.exportSymbols("TPT-HIGH-AVAIL-MIB", tptPerfProtNotifyPacketLoss=tptPerfProtNotifyPacketLoss, highAvailZeroPowerState=highAvailZeroPowerState, ZphaAction=ZphaAction, highAvailZeroPowerSegment=highAvailZeroPowerSegment, highAvailFaultCause=highAvailFaultCause, highAvailThresholdPercent=highAvailThresholdPercent, tptZphaNotifyTimeStamp=tptZphaNotifyTimeStamp, highAvailZeroPowerPresence=highAvailZeroPowerPresence, tptZphaNotifyNewState=tptZphaNotifyNewState, highAvailFaultState=highAvailFaultState, tptIhaNotifyFaultState=tptIhaNotifyFaultState, tpt_high_avail_objs=tpt_high_avail_objs, tptPerfProtNotify=tptPerfProtNotify, tptIhaNotifyTimeStamp=tptIhaNotifyTimeStamp, tptIhaNotifyFaultCause=tptIhaNotifyFaultCause, tptPerfProtNotifyLossThreshold=tptPerfProtNotifyLossThreshold, highAvailTransparentState=highAvailTransparentState, tptPerfProtNotifyDeviceID=tptPerfProtNotifyDeviceID, ConnectionState=ConnectionState, tptTrhaNotifyNewState=tptTrhaNotifyNewState, highAvailZeroPowerAction=highAvailZeroPowerAction, tptPerfProtNotifyPhase=tptPerfProtNotifyPhase, tptZphaNotify=tptZphaNotify, highAvailTransparentPartner=highAvailTransparentPartner, highAvailZeroPowerIndex=highAvailZeroPowerIndex, tptIhaNotify=tptIhaNotify, PYSNMP_MODULE_ID=tpt_high_avail_objs, highAvailTransparentEnabled=highAvailTransparentEnabled, highAvailEnabled=highAvailEnabled, highAvailZeroPowerEntry=highAvailZeroPowerEntry, ZphaMode=ZphaMode, highAvailZeroPowerTable=highAvailZeroPowerTable, ZphaPresent=ZphaPresent, highAvailZeroPowerMode=highAvailZeroPowerMode, PerfProtPhase=PerfProtPhase, FaultCause=FaultCause, tptTrhaNotifyDeviceID=tptTrhaNotifyDeviceID, highAvailThresholdEnabled=highAvailThresholdEnabled, highAvailZeroPowerActive=highAvailZeroPowerActive, tptZphaNotifySegmentName=tptZphaNotifySegmentName, highAvailZeroPowerQuantity=highAvailZeroPowerQuantity, ZphaState=ZphaState, FaultState=FaultState, tptPerfProtNotifyTimeStamp=tptPerfProtNotifyTimeStamp, tptPerfProtNotifyDuration=tptPerfProtNotifyDuration, tptPerfProtNotifyMissedAlerts=tptPerfProtNotifyMissedAlerts, tptZphaNotifyDeviceID=tptZphaNotifyDeviceID, tptTrhaNotifyTimeStamp=tptTrhaNotifyTimeStamp, tptTrhaNotify=tptTrhaNotify, highAvailTimeStamp=highAvailTimeStamp, tptIhaNotifyDeviceID=tptIhaNotifyDeviceID)
