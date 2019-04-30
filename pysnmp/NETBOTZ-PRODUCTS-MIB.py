#
# PySNMP MIB module NETBOTZ-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETBOTZ-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
netBotz_products, = mibBuilder.importSymbols("NETBOTZ-MIB", "netBotz-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Unsigned32, ModuleIdentity, Counter32, MibIdentifier, iso, Counter64, TimeTicks, ObjectIdentity, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Unsigned32", "ModuleIdentity", "Counter32", "MibIdentifier", "iso", "Counter64", "TimeTicks", "ObjectIdentity", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netBotz_prd_bot = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 10)).setLabel("netBotz-prd-bot")
netBotz_prd_crawlers = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 20)).setLabel("netBotz-prd-crawlers")
netBotz_prd_crltrap = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 21)).setLabel("netBotz-prd-crltrap")
netBotz_prd_WallBotz_300 = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 1000)).setLabel("netBotz-prd-WallBotz-300")
netBotz_prd_RackBotz_300 = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 1001)).setLabel("netBotz-prd-RackBotz-300")
netBotz_prd_RackBotz_300U = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 1002)).setLabel("netBotz-prd-RackBotz-300U")
netBotz_prd_RackBotz_303 = MibIdentifier((1, 3, 6, 1, 4, 1, 5528, 30, 1006)).setLabel("netBotz-prd-RackBotz-303")
mibBuilder.exportSymbols("NETBOTZ-PRODUCTS-MIB", netBotz_prd_bot=netBotz_prd_bot, netBotz_prd_WallBotz_300=netBotz_prd_WallBotz_300, netBotz_prd_crltrap=netBotz_prd_crltrap, netBotz_prd_RackBotz_303=netBotz_prd_RackBotz_303, netBotz_prd_crawlers=netBotz_prd_crawlers, netBotz_prd_RackBotz_300=netBotz_prd_RackBotz_300, netBotz_prd_RackBotz_300U=netBotz_prd_RackBotz_300U)
