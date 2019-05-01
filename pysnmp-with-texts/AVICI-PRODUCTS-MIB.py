#
# PySNMP MIB module AVICI-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVICI-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:32:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
aviciMibs, aviciProducts = mibBuilder.importSymbols("AVICI-SMI", "aviciMibs", "aviciProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, NotificationType, Integer32, IpAddress, Bits, MibIdentifier, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "NotificationType", "Integer32", "IpAddress", "Bits", "MibIdentifier", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aviciProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2474, 1, 1))
if mibBuilder.loadTexts: aviciProductsMIB.setLastUpdated('000524190000Z')
if mibBuilder.loadTexts: aviciProductsMIB.setOrganization('Avici Systems, Inc.')
if mibBuilder.loadTexts: aviciProductsMIB.setContactInfo(' Avici Systems, Inc. 101 Billerica Avenue North Billerica, MA 01862-1256 (978) 964-2000 (978) 964-2100 (fax) snmp@avici.com')
if mibBuilder.loadTexts: aviciProductsMIB.setDescription('This MIB module contains the definitions for all Avici products.')
aviciTSR = MibIdentifier((1, 3, 6, 1, 4, 1, 2474, 2, 1))
mibBuilder.exportSymbols("AVICI-PRODUCTS-MIB", aviciProductsMIB=aviciProductsMIB, aviciTSR=aviciTSR, PYSNMP_MODULE_ID=aviciProductsMIB)
