#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-SnmpTestMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-SnmpTestMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:21:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, ObjectIdentity, Unsigned32, TimeTicks, Counter64, NotificationType, Gauge32, MibIdentifier, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter64", "NotificationType", "Gauge32", "MibIdentifier", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmpTestMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 104))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-SnmpTestMIB", snmpTestMIB=snmpTestMIB)
