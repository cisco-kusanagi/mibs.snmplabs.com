#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PerfHist-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, MibIdentifier, ModuleIdentity, Unsigned32, Integer32, Gauge32, IpAddress, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Counter32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Integer32", "Gauge32", "IpAddress", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Counter32", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
perfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 58))
if mibBuilder.loadTexts: perfHistTCMIB.setLastUpdated('9811071100Z')
if mibBuilder.loadTexts: perfHistTCMIB.setOrganization('IETF AToMMIB and TrunkMIB WGs')
if mibBuilder.loadTexts: perfHistTCMIB.setContactInfo('Kaj Tesink Postal: Bellcore 331 Newman Springs Road Red Bank, NJ 07701 USA Tel: +1 732 758 5254 Fax: +1 732 758 2269 E-mail: kaj@bellcore.com')
if mibBuilder.loadTexts: perfHistTCMIB.setDescription('This MIB Module provides Textual Conventions to be used by systems supporting 15 minute based performance history counts.')
class PerfCurrentCount(TextualConvention, Gauge32):
    description = 'A counter associated with a performance measurement in a current 15 minute measurement interval. The value of this counter starts from zero and is increased when associated events occur, until the end of the 15 minute interval. At that time the value of the counter is stored in the first 15 minute history interval, and the CurrentCount is restarted at zero. In the case where the agent has no valid data available for the current interval the corresponding object instance is not available and upon a retrieval request a corresponding error message shall be returned to indicate that this instance does not exist (for example, a noSuchName error for SNMPv1 and a noSuchInstance for SNMPv2 GET operation).'
    status = 'current'

class PerfIntervalCount(TextualConvention, Gauge32):
    description = 'A counter associated with a performance measurement in a previous 15 minute measurement interval. In the case where the agent has no valid data available for a particular interval the corresponding object instance is not available and upon a retrieval request a corresponding error message shall be returned to indicate that this instance does not exist (for example, a noSuchName error for SNMPv1 and a noSuchInstance for SNMPv2 GET operation). In a system supporting a history of n intervals with IntervalCount(1) and IntervalCount(n) the most and least recent intervals respectively, the following applies at the end of a 15 minute interval: - discard the value of IntervalCount(n) - the value of IntervalCount(i) becomes that of IntervalCount(i-1) for n >= i > 1 - the value of IntervalCount(1) becomes that of CurrentCount - the TotalCount, if supported, is adjusted.'
    status = 'current'

class PerfTotalCount(TextualConvention, Gauge32):
    description = 'A counter associated with a performance measurements aggregating the previous valid 15 minute measurement intervals. (Intervals for which no valid data was available are not counted)'
    status = 'current'

mibBuilder.exportSymbols("PerfHist-TC-MIB", PerfIntervalCount=PerfIntervalCount, PerfCurrentCount=PerfCurrentCount, PYSNMP_MODULE_ID=perfHistTCMIB, perfHistTCMIB=perfHistTCMIB, PerfTotalCount=PerfTotalCount)
