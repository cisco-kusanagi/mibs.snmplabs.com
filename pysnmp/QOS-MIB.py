#
# PySNMP MIB module QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/QOS-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:32:57 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, ObjectIdentity, Counter64, NotificationType, Unsigned32, Bits, Counter32, IpAddress, MibIdentifier, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ObjectIdentity", "Counter64", "NotificationType", "Unsigned32", "Bits", "Counter32", "IpAddress", "MibIdentifier", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
qos = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 3))
if mibBuilder.loadTexts: qos.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: qos.setOrganization('Quanta Computer Inc.')
mibBuilder.exportSymbols("QOS-MIB", PYSNMP_MODULE_ID=qos, qos=qos)
