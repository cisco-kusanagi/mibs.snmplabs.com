#
# PySNMP MIB module QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/QOS-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:35:43 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, ModuleIdentity, ObjectIdentity, MibIdentifier, NotificationType, IpAddress, TimeTicks, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "NotificationType", "IpAddress", "TimeTicks", "Bits", "iso")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
qos = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 3))
if mibBuilder.loadTexts: qos.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: qos.setOrganization('Quanta Computer Inc.')
if mibBuilder.loadTexts: qos.setContactInfo(' Customer Support Postal: Quanta Computer Inc. 4, Wen Ming 1 St., Kuei Shan Hsiang, Tao Yuan Shien, Taiwan, R.O.C. Tel: +886 3 328 0050 E-Mail: strong.chen@quantatw.com')
if mibBuilder.loadTexts: qos.setDescription('The MIB definitaions for Quality of Service Flex package.')
mibBuilder.exportSymbols("QOS-MIB", qos=qos, PYSNMP_MODULE_ID=qos)
