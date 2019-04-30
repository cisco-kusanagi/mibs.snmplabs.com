#
# PySNMP MIB module DGS-6600-ID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS-6600-ID-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:30:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
dlink_products, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, Unsigned32, ObjectIdentity, TimeTicks, Integer32, Bits, Counter32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "TimeTicks", "Integer32", "Bits", "Counter32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dgs6600Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120))
dgs6604 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 1))
dgs6608 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 2))
dgs6600Private = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100))
dgs6600_system = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1)).setLabel("dgs6600-system")
dgs6600_l2 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 2)).setLabel("dgs6600-l2")
dgs6600_l3 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 3)).setLabel("dgs6600-l3")
dgs6600_mpls = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4)).setLabel("dgs6600-mpls")
dgs6600_qosacl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 5)).setLabel("dgs6600-qosacl")
dgs6600_security = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 6)).setLabel("dgs6600-security")
dgs6600_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 7)).setLabel("dgs6600-mgmt")
dgs6600_others = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 8)).setLabel("dgs6600-others")
mibBuilder.exportSymbols("DGS-6600-ID-MIB", dgs6600Private=dgs6600Private, dgs6600_others=dgs6600_others, dgs6600Series=dgs6600Series, dgs6600_security=dgs6600_security, dgs6600_mgmt=dgs6600_mgmt, dgs6600_mpls=dgs6600_mpls, dgs6600_system=dgs6600_system, dgs6604=dgs6604, dgs6600_l2=dgs6600_l2, dgs6600_qosacl=dgs6600_qosacl, dgs6608=dgs6608, dgs6600_l3=dgs6600_l3)
