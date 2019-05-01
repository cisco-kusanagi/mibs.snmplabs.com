#
# PySNMP MIB module SW36XXPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW36XXPRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:46:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, TimeTicks, Unsigned32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Counter32, ModuleIdentity, Integer32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "TimeTicks", "Unsigned32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Counter32", "ModuleIdentity", "Integer32", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_ProjectXStackIISeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70)).setLabel("dlink-ProjectXStackIISeriesProd")
dlink_Dgs3650 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 5)).setLabel("dlink-Dgs3650")
dlink_Dgs3627 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 6)).setLabel("dlink-Dgs3627")
dlink_Dgs3627g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 8)).setLabel("dlink-Dgs3627g")
dlink_Dgs3612g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 9)).setLabel("dlink-Dgs3612g")
dlink_Dgs3612 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 70, 10)).setLabel("dlink-Dgs3612")
dgsProjectXStackIISeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70))
dgs3650 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 5))
dgs3627 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 6))
dgs3627g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 8))
dgs3612g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 9))
dgs3612 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 70, 10))
mibBuilder.exportSymbols("SW36XXPRIMGMT-MIB", dgsProjectXStackIISeriesProd=dgsProjectXStackIISeriesProd, dgs3650=dgs3650, dgs3627=dgs3627, dlink_Dgs3627=dlink_Dgs3627, dlink_Dgs3650=dlink_Dgs3650, dgs3627g=dgs3627g, dlink_ProjectXStackIISeriesProd=dlink_ProjectXStackIISeriesProd, dlink_Dgs3627g=dlink_Dgs3627g, dgs3612g=dgs3612g, dgs3612=dgs3612, dlink_Dgs3612g=dlink_Dgs3612g, dlink_Dgs3612=dlink_Dgs3612)
