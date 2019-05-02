#
# PySNMP MIB module TPT-HIGH-AVAIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-HIGH-AVAIL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, Bits, ObjectIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ModuleIdentity, Integer32, IpAddress, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Bits", "ObjectIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ModuleIdentity", "Integer32", "IpAddress", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
EnabledOrNot, = mibBuilder.importSymbols("TPT-PORT-CONFIG-MIB", "EnabledOrNot")
tpt_tpa_eventsV2, tpt_tpa_objs, tpt_tpa_unkparams = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-eventsV2", "tpt-tpa-objs", "tpt-tpa-unkparams")
tpt_high_avail_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6)).setLabel("tpt-high-avail-objs")
tpt_high_avail_objs.setRevisions(('2016-09-08 18:54', '2016-05-25 18:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_high_avail_objs.setRevisionsDescriptions(('Added new FaultCause values to support TPS. Updated description of highAvailTransparentPartner.', 'Updated copyright information. Minor MIB syntax fixes.',))
if mibBuilder.loadTexts: tpt_high_avail_objs.setLastUpdated('201609081854Z')
if mibBuilder.loadTexts: tpt_high_avail_objs.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_high_avail_objs.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_high_avail_objs.setDescription("Device information related to high availability. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
class FaultState(TextualConvention, Integer32):
    description = 'The current fault state of the device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("normal", 0), ("fallback", 1))

class FaultCause(TextualConvention, Integer32):
    description = 'The reason for the current fault state of the device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("none", 0), ("suspended-task", 1), ("out-of-memory", 2), ("hardware-breakpoint", 3), ("tse-failure", 4), ("watchdog-timeout", 5), ("user-reset", 6), ("user-fallback", 7), ("threshold-failure", 8), ("software-watchdog-timeout", 9), ("oam-fault", 10), ("hard-disk-disable", 11), ("initialization-failure", 12), ("internal-link-failure", 13), ("multiple-fan-failures", 14), ("packet-egress-integrity", 15), ("stack-master", 16), ("waiting-on-stack", 17), ("spike-reboot-or-halt", 18), ("process-error", 19), ("low-health-score", 20))

class ConnectionState(TextualConvention, Integer32):
    description = 'State of the connection between a device and its transparent HA partner.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-connected", 0), ("unresponsive", 1), ("connected", 2))

class PerfProtPhase(TextualConvention, Integer32):
    description = 'The performance protection phase (entering, continuing, or exiting).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("entering", 1), ("continuing", 2), ("exiting", 3))

class ZphaState(TextualConvention, Integer32):
    description = 'Whether ZPHA bypass is currently in effect.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("normal", 0), ("ips-bypass", 1))

class ZphaAction(TextualConvention, Integer32):
    description = 'The ZPHA action (normal or bypass).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("normal", 1), ("bypass", 2))

class ZphaMode(TextualConvention, Integer32):
    description = 'The ZPHA fiber mode (single or multi).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("single", 2), ("multi", 3))

class ZphaPresent(TextualConvention, Integer32):
    description = 'Whether segmental ZPHA is supported on the device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("absent", 0), ("present", 1))

highAvailTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailTimeStamp.setStatus('current')
if mibBuilder.loadTexts: highAvailTimeStamp.setDescription('The time of the last transition of the fault state (in seconds since January 1, 1970). This value is zero if the fault state has not changed since the last reboot.')
highAvailFaultState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 2), FaultState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailFaultState.setStatus('current')
if mibBuilder.loadTexts: highAvailFaultState.setDescription('The current fault state of the device.')
highAvailFaultCause = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 3), FaultCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailFaultCause.setStatus('current')
if mibBuilder.loadTexts: highAvailFaultCause.setDescription('The reason for the current fault state of the device.')
highAvailThresholdEnabled = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 4), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailThresholdEnabled.setStatus('current')
if mibBuilder.loadTexts: highAvailThresholdEnabled.setDescription('The current fallback threshold enabled setting for the device.')
highAvailThresholdPercent = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailThresholdPercent.setStatus('current')
if mibBuilder.loadTexts: highAvailThresholdPercent.setDescription('If the fallback threshold is enabled, the percent (0-100) packet loss at which the device is configured to enter the fallback state.')
highAvailEnabled = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 6), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailEnabled.setStatus('current')
if mibBuilder.loadTexts: highAvailEnabled.setDescription('Whether intrinisic high availability is enabled for this device.')
highAvailTransparentState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 7), ConnectionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailTransparentState.setStatus('current')
if mibBuilder.loadTexts: highAvailTransparentState.setDescription("State of the connection to the device's transparent HA partner.")
highAvailTransparentEnabled = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 8), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailTransparentEnabled.setStatus('current')
if mibBuilder.loadTexts: highAvailTransparentEnabled.setDescription('Whether transparent high availability is enabled for this device.')
highAvailTransparentPartner = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailTransparentPartner.setStatus('current')
if mibBuilder.loadTexts: highAvailTransparentPartner.setDescription("Network address OR serial number of the device's transparent HA partner.")
highAvailZeroPowerState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 10), ZphaState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerState.setStatus('current')
if mibBuilder.loadTexts: highAvailZeroPowerState.setDescription('The current zero-power HA state of the device.')
highAvailZeroPowerQuantity = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerQuantity.setStatus('current')
if mibBuilder.loadTexts: highAvailZeroPowerQuantity.setDescription('The number of segments with zero-power HA modules.')
highAvailZeroPowerTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12), )
if mibBuilder.loadTexts: highAvailZeroPowerTable.setStatus('current')
if mibBuilder.loadTexts: highAvailZeroPowerTable.setDescription('Table of IP addresses on the device and their attributes.')
highAvailZeroPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1), ).setIndexNames((0, "TPT-HIGH-AVAIL-MIB", "highAvailZeroPowerIndex"))
if mibBuilder.loadTexts: highAvailZeroPowerEntry.setStatus('current')
if mibBuilder.loadTexts: highAvailZeroPowerEntry.setDescription('An entry in the host IP address table. Rows cannot be created or deleted.')
highAvailZeroPowerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 1), Unsigned32())
if mibBuilder.loadTexts: highAvailZeroPowerIndex.setStatus('current')
if mibBuilder.loadTexts: highAvailZeroPowerIndex.setDescription('Index into the ZPHA table, starting with 1.')
highAvailZeroPowerSegment = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerSegment.setStatus('current')
if mibBuilder.loadTexts: highAvailZeroPowerSegment.setDescription('The name of the segment to which the ZPHA is attached.')
highAvailZeroPowerActive = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 3), ZphaState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerActive.setStatus('current')
if mibBuilder.loadTexts: highAvailZeroPowerActive.setDescription('Whether the ZPHA is currently active on this segment.')
highAvailZeroPowerAction = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 4), ZphaAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerAction.setStatus('current')
if mibBuilder.loadTexts: highAvailZeroPowerAction.setDescription('The action (usually bypass) that the segment takes when ZPHA is active.')
highAvailZeroPowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 5), ZphaMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerMode.setStatus('current')
if mibBuilder.loadTexts: highAvailZeroPowerMode.setDescription('The fiber mode (single or multi) of this ZPHA.')
highAvailZeroPowerPresence = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 13), ZphaPresent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: highAvailZeroPowerPresence.setStatus('current')
if mibBuilder.loadTexts: highAvailZeroPowerPresence.setDescription('An indication of whether ZPHA is supported on the device.')
tptIhaNotifyDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 81), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptIhaNotifyDeviceID.setStatus('current')
if mibBuilder.loadTexts: tptIhaNotifyDeviceID.setDescription('The unique identifier of the device sending this notification.')
tptIhaNotifyTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 82), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptIhaNotifyTimeStamp.setStatus('current')
if mibBuilder.loadTexts: tptIhaNotifyTimeStamp.setDescription('The time of this notification (in seconds since January 1, 1970).')
tptIhaNotifyFaultState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 83), FaultState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptIhaNotifyFaultState.setStatus('current')
if mibBuilder.loadTexts: tptIhaNotifyFaultState.setDescription('The current fault state of the device.')
tptIhaNotifyFaultCause = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 84), FaultCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptIhaNotifyFaultCause.setStatus('current')
if mibBuilder.loadTexts: tptIhaNotifyFaultCause.setDescription('The reason for the current fault state of the device.')
tptIhaNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 15)).setObjects(("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyDeviceID"), ("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyTimeStamp"), ("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyFaultState"), ("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyFaultCause"))
if mibBuilder.loadTexts: tptIhaNotify.setStatus('current')
if mibBuilder.loadTexts: tptIhaNotify.setDescription('Notification: Used to inform the management station of changes in the intrinsic HA fault state on the device.')
tptTrhaNotifyDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 86), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTrhaNotifyDeviceID.setStatus('current')
if mibBuilder.loadTexts: tptTrhaNotifyDeviceID.setDescription('The unique identifier of the device sending this notification.')
tptTrhaNotifyTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 87), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTrhaNotifyTimeStamp.setStatus('current')
if mibBuilder.loadTexts: tptTrhaNotifyTimeStamp.setDescription('The time of this notification (in seconds since January 1, 1970).')
tptTrhaNotifyNewState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 88), ConnectionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTrhaNotifyNewState.setStatus('current')
if mibBuilder.loadTexts: tptTrhaNotifyNewState.setDescription('The new transparent HA state of the device.')
tptTrhaNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 18)).setObjects(("TPT-HIGH-AVAIL-MIB", "tptTrhaNotifyDeviceID"), ("TPT-HIGH-AVAIL-MIB", "tptTrhaNotifyTimeStamp"), ("TPT-HIGH-AVAIL-MIB", "tptTrhaNotifyNewState"))
if mibBuilder.loadTexts: tptTrhaNotify.setStatus('current')
if mibBuilder.loadTexts: tptTrhaNotify.setDescription('Notification: Used to inform the management station of changes in the transparent HA state on the device.')
tptZphaNotifyDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 161), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptZphaNotifyDeviceID.setStatus('current')
if mibBuilder.loadTexts: tptZphaNotifyDeviceID.setDescription('The unique identifier of the device sending this notification.')
tptZphaNotifyTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 162), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptZphaNotifyTimeStamp.setStatus('current')
if mibBuilder.loadTexts: tptZphaNotifyTimeStamp.setDescription('The time of this notification (in seconds since January 1, 1970).')
tptZphaNotifySegmentName = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 163), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptZphaNotifySegmentName.setStatus('current')
if mibBuilder.loadTexts: tptZphaNotifySegmentName.setDescription('The name of the segment whose ZPHA changed state, or an empty string to indicate the external ZPHA.')
tptZphaNotifyNewState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 164), ZphaState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptZphaNotifyNewState.setStatus('current')
if mibBuilder.loadTexts: tptZphaNotifyNewState.setDescription('The new state of the ZPHA that has changed.')
tptZphaNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 24)).setObjects(("TPT-HIGH-AVAIL-MIB", "tptZphaNotifyDeviceID"), ("TPT-HIGH-AVAIL-MIB", "tptZphaNotifyTimeStamp"), ("TPT-HIGH-AVAIL-MIB", "tptZphaNotifySegmentName"), ("TPT-HIGH-AVAIL-MIB", "tptZphaNotifyNewState"))
if mibBuilder.loadTexts: tptZphaNotify.setStatus('current')
if mibBuilder.loadTexts: tptZphaNotify.setDescription('Notification: Used to inform the management station of changes in a ZPHA state on the device.')
tptPerfProtNotifyDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 141), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyDeviceID.setStatus('current')
if mibBuilder.loadTexts: tptPerfProtNotifyDeviceID.setDescription('The unique identifier of the device sending this notification.')
tptPerfProtNotifyTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 142), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyTimeStamp.setStatus('current')
if mibBuilder.loadTexts: tptPerfProtNotifyTimeStamp.setDescription('The time of this notification (in seconds since January 1, 1970).')
tptPerfProtNotifyPhase = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 143), PerfProtPhase()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyPhase.setStatus('current')
if mibBuilder.loadTexts: tptPerfProtNotifyPhase.setDescription('Whether entering, remaining in, or exiting performance protection mode.')
tptPerfProtNotifyPacketLoss = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 144), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyPacketLoss.setStatus('current')
if mibBuilder.loadTexts: tptPerfProtNotifyPacketLoss.setDescription('The current packet loss rate per thousand (percent * 10). When exiting performance protection mode, this value is 0.')
tptPerfProtNotifyLossThreshold = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 145), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyLossThreshold.setStatus('current')
if mibBuilder.loadTexts: tptPerfProtNotifyLossThreshold.setDescription('The current packet loss threshold per thousand (percent * 10).')
tptPerfProtNotifyDuration = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 146), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyDuration.setStatus('current')
if mibBuilder.loadTexts: tptPerfProtNotifyDuration.setDescription('The number of seconds performance protection will be in force.')
tptPerfProtNotifyMissedAlerts = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 147), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptPerfProtNotifyMissedAlerts.setStatus('current')
if mibBuilder.loadTexts: tptPerfProtNotifyMissedAlerts.setDescription('The number of alerts missed during the performance protection period. When entering performance protection mode, this value is 0.')
tptPerfProtNotify = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 21)).setObjects(("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyDeviceID"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyTimeStamp"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyPhase"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyPacketLoss"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyLossThreshold"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyDuration"), ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyMissedAlerts"))
if mibBuilder.loadTexts: tptPerfProtNotify.setStatus('current')
if mibBuilder.loadTexts: tptPerfProtNotify.setDescription('Notification: Used to inform the management station of changes in performance protection on the device.')
mibBuilder.exportSymbols("TPT-HIGH-AVAIL-MIB", FaultState=FaultState, tptTrhaNotify=tptTrhaNotify, highAvailZeroPowerMode=highAvailZeroPowerMode, highAvailZeroPowerEntry=highAvailZeroPowerEntry, tptPerfProtNotify=tptPerfProtNotify, tptTrhaNotifyTimeStamp=tptTrhaNotifyTimeStamp, tpt_high_avail_objs=tpt_high_avail_objs, tptIhaNotifyFaultCause=tptIhaNotifyFaultCause, tptPerfProtNotifyMissedAlerts=tptPerfProtNotifyMissedAlerts, ZphaMode=ZphaMode, tptZphaNotifyDeviceID=tptZphaNotifyDeviceID, tptPerfProtNotifyPacketLoss=tptPerfProtNotifyPacketLoss, FaultCause=FaultCause, ZphaPresent=ZphaPresent, PYSNMP_MODULE_ID=tpt_high_avail_objs, tptZphaNotifySegmentName=tptZphaNotifySegmentName, highAvailTransparentState=highAvailTransparentState, highAvailZeroPowerQuantity=highAvailZeroPowerQuantity, tptIhaNotifyTimeStamp=tptIhaNotifyTimeStamp, ZphaAction=ZphaAction, tptTrhaNotifyNewState=tptTrhaNotifyNewState, tptTrhaNotifyDeviceID=tptTrhaNotifyDeviceID, tptPerfProtNotifyLossThreshold=tptPerfProtNotifyLossThreshold, tptZphaNotify=tptZphaNotify, tptPerfProtNotifyDeviceID=tptPerfProtNotifyDeviceID, ConnectionState=ConnectionState, tptZphaNotifyTimeStamp=tptZphaNotifyTimeStamp, highAvailZeroPowerActive=highAvailZeroPowerActive, tptIhaNotifyFaultState=tptIhaNotifyFaultState, highAvailThresholdEnabled=highAvailThresholdEnabled, highAvailZeroPowerTable=highAvailZeroPowerTable, highAvailTransparentEnabled=highAvailTransparentEnabled, highAvailZeroPowerSegment=highAvailZeroPowerSegment, highAvailFaultCause=highAvailFaultCause, tptPerfProtNotifyDuration=tptPerfProtNotifyDuration, highAvailThresholdPercent=highAvailThresholdPercent, highAvailZeroPowerState=highAvailZeroPowerState, highAvailEnabled=highAvailEnabled, highAvailTimeStamp=highAvailTimeStamp, tptZphaNotifyNewState=tptZphaNotifyNewState, highAvailZeroPowerAction=highAvailZeroPowerAction, PerfProtPhase=PerfProtPhase, highAvailZeroPowerIndex=highAvailZeroPowerIndex, tptIhaNotify=tptIhaNotify, tptPerfProtNotifyTimeStamp=tptPerfProtNotifyTimeStamp, ZphaState=ZphaState, tptPerfProtNotifyPhase=tptPerfProtNotifyPhase, tptIhaNotifyDeviceID=tptIhaNotifyDeviceID, highAvailFaultState=highAvailFaultState, highAvailZeroPowerPresence=highAvailZeroPowerPresence, highAvailTransparentPartner=highAvailTransparentPartner)
