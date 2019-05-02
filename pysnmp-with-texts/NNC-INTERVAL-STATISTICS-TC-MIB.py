#
# PySNMP MIB module NNC-INTERVAL-STATISTICS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNC-INTERVAL-STATISTICS-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:22:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NncUnsigned32, nncExtensions = mibBuilder.importSymbols("NNCGNI0001-SMI", "NncUnsigned32", "nncExtensions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, Bits, Counter64, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, TimeTicks, Gauge32, ModuleIdentity, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "Bits", "Counter64", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "TimeTicks", "Gauge32", "ModuleIdentity", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nncExtIntvlStats = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 3, 31))
if mibBuilder.loadTexts: nncExtIntvlStats.setLastUpdated('9603211520Z')
if mibBuilder.loadTexts: nncExtIntvlStats.setOrganization('Newbridge Networks Corporation')
if mibBuilder.loadTexts: nncExtIntvlStats.setContactInfo('Newbridge Networks Corporation Postal: 600 March Road Kanata, Ontario Canada K2K 2E6 Phone: +1 613 591 3600 Fax: +1 613 591 3680')
if mibBuilder.loadTexts: nncExtIntvlStats.setDescription('The MIB module containing type definitions common to interval statistics collection mibs.')
class NncExtIntvlStateType(TextualConvention, Integer32):
    description = 'The type describing the state of the interval in the interval statistics interface. Possible states are: normal (1) - normal interval; no change in time and no resets nonexistent (2) - statistics do not exist for this interval userReset (3) - the user has reset statistics collection during this interval start (4) - this is the first interval timeChange (5) - the system time has been changed during this interval'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("normal", 1), ("nonexistent", 2), ("userReset", 3), ("start", 4), ("timeChange", 5))

class NncExtAbsIntvlNumberType(NncUnsigned32):
    description = 'The type describing the absolute interval number of the stats interval in the interval statistics interface. For the short, 15 minutes intervals the possible values are: absolute interval interval index start end ----------------- ------------ 1 00:00 00:15 2 00:15 00:30 3 00:30 00:45 ... ... ... 95 23:30 23:45 96 23:45 00:00 For the long, 1 hour intervals the possible values are: absolute interval interval index start end ----------------- ------------ 1 00:00 01:00 2 01:00 02:00 3 02:00 03:00 ... ... ... 23 22:00 23:00 24 23:00 24:00 For other interval types or interval durations absolute interval index in not defined.'
    status = 'current'

class NncExtRelIntvlNumberType(NncUnsigned32):
    description = 'The type describing the relative interval number of the statistics interval in the interval statistics interface. The values are from 1 to N, where 1 represents the most recently completed interval, 2 represents the second most recently completed interval, etc., and N is the total number of previous intervals supported.'
    status = 'current'

class NncExtIntvlDurationType(NncUnsigned32):
    description = 'The type describing the duration of the statistics interval in the interval statistics interface. The value represents the number of seconds that have elapsed since the beginning of the interval.'
    status = 'current'

mibBuilder.exportSymbols("NNC-INTERVAL-STATISTICS-TC-MIB", PYSNMP_MODULE_ID=nncExtIntvlStats, NncExtIntvlStateType=NncExtIntvlStateType, nncExtIntvlStats=nncExtIntvlStats, NncExtAbsIntvlNumberType=NncExtAbsIntvlNumberType, NncExtIntvlDurationType=NncExtIntvlDurationType, NncExtRelIntvlNumberType=NncExtRelIntvlNumberType)
