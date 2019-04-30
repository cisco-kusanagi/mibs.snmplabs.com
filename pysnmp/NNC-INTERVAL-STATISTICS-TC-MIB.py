#
# PySNMP MIB module NNC-INTERVAL-STATISTICS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNC-INTERVAL-STATISTICS-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
nncExtensions, NncUnsigned32 = mibBuilder.importSymbols("NNCGNI0001-SMI", "nncExtensions", "NncUnsigned32")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Bits, Unsigned32, IpAddress, iso, ModuleIdentity, Counter32, ObjectIdentity, MibIdentifier, Gauge32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Bits", "Unsigned32", "IpAddress", "iso", "ModuleIdentity", "Counter32", "ObjectIdentity", "MibIdentifier", "Gauge32", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nncExtIntvlStats = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 3, 31))
if mibBuilder.loadTexts: nncExtIntvlStats.setLastUpdated('9603211520Z')
if mibBuilder.loadTexts: nncExtIntvlStats.setOrganization('Newbridge Networks Corporation')
class NncExtIntvlStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("normal", 1), ("nonexistent", 2), ("userReset", 3), ("start", 4), ("timeChange", 5))

class NncExtAbsIntvlNumberType(NncUnsigned32):
    status = 'current'

class NncExtRelIntvlNumberType(NncUnsigned32):
    status = 'current'

class NncExtIntvlDurationType(NncUnsigned32):
    status = 'current'

mibBuilder.exportSymbols("NNC-INTERVAL-STATISTICS-TC-MIB", NncExtIntvlDurationType=NncExtIntvlDurationType, nncExtIntvlStats=nncExtIntvlStats, PYSNMP_MODULE_ID=nncExtIntvlStats, NncExtRelIntvlNumberType=NncExtRelIntvlNumberType, NncExtAbsIntvlNumberType=NncExtAbsIntvlNumberType, NncExtIntvlStateType=NncExtIntvlStateType)
