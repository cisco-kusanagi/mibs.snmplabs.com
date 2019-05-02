#
# PySNMP MIB module EXPAND-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXPAND-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
expandProducts, = mibBuilder.importSymbols("EXPAND-NETWORKS-SMI", "expandProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Bits, iso, Unsigned32, Counter32, ObjectIdentity, IpAddress, Integer32, MibIdentifier, Gauge32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Bits", "iso", "Unsigned32", "Counter32", "ObjectIdentity", "IpAddress", "Integer32", "MibIdentifier", "Gauge32", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
accelerator4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 1))
accelerator2700 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 2))
accelerator4800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 3))
accelerator2800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 4))
accelerator1800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 5))
accelerator4802 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 6))
mibBuilder.exportSymbols("EXPAND-PRODUCTS-MIB", accelerator1800=accelerator1800, accelerator4802=accelerator4802, accelerator2700=accelerator2700, accelerator2800=accelerator2800, accelerator4000=accelerator4000, accelerator4800=accelerator4800)
