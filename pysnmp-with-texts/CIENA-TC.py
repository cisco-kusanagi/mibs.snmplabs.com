#
# PySNMP MIB module CIENA-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:49:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, MibIdentifier, IpAddress, Unsigned32, Bits, NotificationType, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibIdentifier", "IpAddress", "Unsigned32", "Bits", "NotificationType", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ObjectIdentity", "TimeTicks")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
class CienaGlobalState(TextualConvention, Integer32):
    description = 'This textual convention enumerates the administrative and operational state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CienaGlobalSeverity(TextualConvention, Integer32):
    description = 'This textual convention enumerates the severity levels.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("none", 0), ("cleared", 1), ("intermediate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6), ("config", 7), ("info", 8), ("debug", 9), ("internal", 10))

class CienaStatsClear(TextualConvention, Integer32):
    description = 'This textual convention enumerates the statistics clear operation if the value is set to 1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("clear", 1))

class CienaMacAddress(MacAddress):
    description = 'This textual convention denotes a MAC address.'
    status = 'current'

mibBuilder.exportSymbols("CIENA-TC", CienaGlobalState=CienaGlobalState, CienaStatsClear=CienaStatsClear, CienaGlobalSeverity=CienaGlobalSeverity, CienaMacAddress=CienaMacAddress)
