#
# PySNMP MIB module HC-PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HC-PerfHist-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Unsigned32, Integer32, iso, Bits, IpAddress, TimeTicks, Gauge32, NotificationType, MibIdentifier, Counter32, mib_2, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Integer32", "iso", "Bits", "IpAddress", "TimeTicks", "Gauge32", "NotificationType", "MibIdentifier", "Counter32", "mib-2", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hcPerfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 107))
hcPerfHistTCMIB.setRevisions(('2004-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hcPerfHistTCMIB.setRevisionsDescriptions(('Initial version, published as RFC 3705.',))
if mibBuilder.loadTexts: hcPerfHistTCMIB.setLastUpdated('200402030000Z')
if mibBuilder.loadTexts: hcPerfHistTCMIB.setOrganization('ADSLMIB Working Group')
if mibBuilder.loadTexts: hcPerfHistTCMIB.setContactInfo('WG-email: adslmib@ietf.org Info: https://www1.ietf.org/mailman/listinfo/adslmib Chair: Mike Sneed Sand Channel Systems Postal: P.O. Box 37324 Raleigh NC 27627-7324 USA Email: sneedmike@hotmail.com Phone: +1 206 600 7022 Co-editor: Bob Ray PESA Switching Systems, Inc. Postal: 330-A Wynn Drive Huntsville, AL 35805 USA Email: rray@pesa.com Phone: +1 256 726 9200 ext. 142 Co-editor: Rajesh Abbi Alcatel USA Postal: 2301 Sugar Bush Road Raleigh, NC 27612-3339 USA Email: Rajesh.Abbi@alcatel.com Phone: +1 919 850 6194 ')
if mibBuilder.loadTexts: hcPerfHistTCMIB.setDescription('This MIB Module provides Textual Conventions to be used by systems supporting 15 minute based performance history counts that require high-capacity counts. Copyright (C) The Internet Society (2004). This version of this MIB module is part of RFC 3705: see the RFC itself for full legal notices.')
class HCPerfValidIntervals(TextualConvention, Integer32):
    description = 'The number of near end intervals for which data was collected. The value of an object with an HCPerfValidIntervals syntax will be 96 unless the measurement was (re-)started within the last 1440 minutes, in which case the value will be the number of complete 15 minute intervals for which the agent has at least some data. In certain cases (e.g., in the case where the agent is a proxy) it is possible that some intervals are unavailable. In this case, this interval is the maximum interval number for which data is available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 96)

class HCPerfInvalidIntervals(TextualConvention, Integer32):
    description = 'The number of near end intervals for which no data is available. The value of an object with an HCPerfInvalidIntervals syntax will typically be zero except in cases where the data for some intervals are not available (e.g., in proxy situations).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 96)

class HCPerfTimeElapsed(TextualConvention, Integer32):
    description = "The number of seconds that have elapsed since the beginning of the current measurement period. If, for some reason, such as an adjustment in the system's time-of-day clock or the addition of a leap second, the duration of the current interval exceeds the maximum value, the agent will return the maximum value. For 15 minute intervals, the range is limited to (0..899). For 24 hour intervals, the range is limited to (0..86399)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 86399)

class HCPerfIntervalThreshold(TextualConvention, Unsigned32):
    description = 'This convention defines a range of values that may be set in a fault threshold alarm control. As the number of seconds in a 15-minute interval numbers at most 900, objects of this type may have a range of 0...900, where the value of 0 disables the alarm.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 900)

class HCPerfCurrentCount(TextualConvention, Counter64):
    description = "A gauge associated with a performance measurement in a current 15 minute measurement interval. The value of an object with an HCPerfCurrentCount syntax starts from zero and is increased when associated events occur, until the end of the 15 minute interval. At that time the value of the gauge is stored in the first 15 minute history interval, and the gauge is restarted at zero. In the case where the agent has no valid data available for the current interval, the corresponding object instance is not available and upon a retrieval request a corresponding error message shall be returned to indicate that this instance does not exist. This count represents a non-negative integer, which may increase or decrease, but shall never exceed 2^64-1 (18446744073709551615 decimal), nor fall below 0. The value of an object with HCPerfCurrentCount syntax assumes its maximum value whenever the underlying count exceeds 2^64-1. If the underlying count subsequently decreases below 2^64-1 (due, e.g., to a retroactive adjustment as a result of entering or exiting unavailable time), then the object's value also decreases. Note that this TC is not strictly supported in SMIv2, because the 'always increasing' and 'counter wrap' semantics associated with the Counter64 base type are not preserved. It is possible that management applications which rely solely upon the (Counter64) ASN.1 tag to determine object semantics will mistakenly operate upon objects of this type as they would for Counter64 objects. This textual convention represents a limited and short- term solution, and may be deprecated as a long term solution is defined and deployed to replace it."
    status = 'current'

class HCPerfIntervalCount(TextualConvention, Counter64):
    description = "A gauge associated with a performance measurement in a previous 15 minute measurement interval. In the case where the agent has no valid data available for a particular interval, the corresponding object instance is not available and upon a retrieval request a corresponding error message shall be returned to indicate that this instance does not exist. Let X be an object with HCPerfIntervalCount syntax. Let Y be an object with HCPerfCurrentCount syntax. Let Z be an object with HCPerfTotalCount syntax. Then, in a system supporting a history of n intervals with X(1) and X(n) the most and least recent intervals respectively, the following applies at the end of a 15 minute interval: - discard the value of X(n) - the value of X(i) becomes that of X(i-1) for n >= i > 1 - the value of X(1) becomes that of Y. - the value of Z, if supported, is adjusted. This count represents a non-negative integer, which may increase or decrease, but shall never exceed 2^64-1 (18446744073709551615 decimal), nor fall below 0. The value of an object with HCPerfIntervalCount syntax assumes its maximum value whenever the underlying count exceeds 2^64-1. If the underlying count subsequently decreases below 2^64-1 (due, e.g., to a retroactive adjustment as a result of entering or exiting unavailable time), then the value of the object also decreases. Note that this TC is not strictly supported in SMIv2, because the 'always increasing' and 'counter wrap' semantics associated with the Counter64 base type are not preserved. It is possible that management applications which rely solely upon the (Counter64) ASN.1 tag to determine object semantics will mistakenly operate upon objects of this type as they would for Counter64 objects. This textual convention represents a limited and short- term solution, and may be deprecated as a long term solution is defined and deployed to replace it."
    status = 'current'

class HCPerfTotalCount(TextualConvention, Counter64):
    description = "A gauge representing the aggregate of previous valid 15 minute measurement intervals. Intervals for which no valid data was available are not counted. This count represents a non-negative integer, which may increase or decrease, but shall never exceed 2^64-1 (18446744073709551615 decimal), nor fall below 0. The value of an object with HCPerfTotalCount syntax assumes its maximum value whenever the underlying count exceeds 2^64-1. If the underlying count subsequently decreases below 2^64-1 (due, e.g., to a retroactive adjustment as a result of entering or exiting unavailable time), then the object's value also decreases. Note that this TC is not strictly supported in SMIv2, because the 'always increasing' and 'counter wrap' semantics associated with the Counter64 base type are not preserved. It is possible that management applications which rely solely upon the (Counter64) ASN.1 tag to determine object semantics will mistakenly operate upon objects of this type as they would for Counter64 objects. This textual convention represents a limited and short- term solution, and may be deprecated as a long term solution is defined and deployed to replace it."
    status = 'current'

mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", HCPerfInvalidIntervals=HCPerfInvalidIntervals, HCPerfCurrentCount=HCPerfCurrentCount, PYSNMP_MODULE_ID=hcPerfHistTCMIB, HCPerfValidIntervals=HCPerfValidIntervals, HCPerfIntervalCount=HCPerfIntervalCount, HCPerfTotalCount=HCPerfTotalCount, HCPerfIntervalThreshold=HCPerfIntervalThreshold, hcPerfHistTCMIB=hcPerfHistTCMIB, HCPerfTimeElapsed=HCPerfTimeElapsed)
