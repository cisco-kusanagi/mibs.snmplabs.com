#
# PySNMP MIB module BCSI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BCSI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:36:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, Integer32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, enterprises, IpAddress, NotificationType, Unsigned32, MibIdentifier, Counter32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Integer32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "enterprises", "IpAddress", "NotificationType", "Unsigned32", "MibIdentifier", "Counter32", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcsi = ModuleIdentity((1, 3, 6, 1, 4, 1, 14501))
if mibBuilder.loadTexts: bcsi.setLastUpdated('201308161500Z')
if mibBuilder.loadTexts: bcsi.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: bcsi.setContactInfo('support@bluecoat.com http://www.bluecoat.com')
if mibBuilder.loadTexts: bcsi.setDescription('The root MIB module for Blue Coat Systems.')
mibBuilder.exportSymbols("BCSI-MIB", PYSNMP_MODULE_ID=bcsi, bcsi=bcsi)
