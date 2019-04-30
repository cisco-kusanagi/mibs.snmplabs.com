#
# PySNMP MIB module CIENA-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 17:31:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, ObjectIdentity, Bits, ModuleIdentity, IpAddress, Gauge32, Integer32, TimeTicks, NotificationType, Unsigned32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "ObjectIdentity", "Bits", "ModuleIdentity", "IpAddress", "Gauge32", "Integer32", "TimeTicks", "NotificationType", "Unsigned32", "iso", "Counter32")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
class CienaGlobalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CienaGlobalSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("none", 0), ("cleared", 1), ("intermediate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6), ("config", 7), ("info", 8), ("debug", 9), ("internal", 10))

class CienaStatsClear(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("clear", 1))

class CienaMacAddress(MacAddress):
    status = 'current'

mibBuilder.exportSymbols("CIENA-TC", CienaGlobalState=CienaGlobalState, CienaStatsClear=CienaStatsClear, CienaGlobalSeverity=CienaGlobalSeverity, CienaMacAddress=CienaMacAddress)
