#
# PySNMP MIB module EXPAND-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXPAND-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:52:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
expandProducts, = mibBuilder.importSymbols("EXPAND-NETWORKS-SMI", "expandProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, IpAddress, iso, ObjectIdentity, Counter32, TimeTicks, Counter64, ModuleIdentity, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "IpAddress", "iso", "ObjectIdentity", "Counter32", "TimeTicks", "Counter64", "ModuleIdentity", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
accelerator4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 1))
accelerator2700 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 2))
accelerator4800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 3))
accelerator2800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 4))
accelerator1800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 5))
accelerator4802 = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2, 6))
mibBuilder.exportSymbols("EXPAND-PRODUCTS-MIB", accelerator1800=accelerator1800, accelerator4000=accelerator4000, accelerator2700=accelerator2700, accelerator2800=accelerator2800, accelerator4802=accelerator4802, accelerator4800=accelerator4800)
