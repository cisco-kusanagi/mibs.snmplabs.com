#
# PySNMP MIB module COLUBRIS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:25:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
colubrisProducts, colubrisModules = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisProducts", "colubrisModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, Bits, IpAddress, iso, ModuleIdentity, Gauge32, TimeTicks, NotificationType, Integer32, Unsigned32, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Bits", "IpAddress", "iso", "ModuleIdentity", "Gauge32", "TimeTicks", "NotificationType", "Integer32", "Unsigned32", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubrisProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 4, 2))
if mibBuilder.loadTexts: colubrisProductsMIB.setLastUpdated('201008260000Z')
if mibBuilder.loadTexts: colubrisProductsMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisProductsMIB.setContactInfo('Colubris Networks Postal: 200 West Street Ste 300 Waltham, Massachusetts 02451-1121 UNITED STATES Phone: +1 781 684 0001 Fax: +1 781 684 0009 E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisProductsMIB.setDescription('Colubris Networks Product Identifiers.')
colubrisCN1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 1))
colubrisCN1000HEREUARE = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 2))
colubrisCN1050 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 3))
colubrisCN1054 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 4))
colubrisCN3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 5))
colubrisCN100HEREUARE = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 6))
colubrisCN100TRAVELNET = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 7))
colubrisCN300 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 8))
colubrisCN1150 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 9))
colubrisCN3100 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 10))
colubrisCN1000LIGHT = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 11))
colubrisCN3500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 12))
colubrisCN310 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 13))
colubrisCN1500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 14))
colubrisCN1550 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 15))
colubrisCN3200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 16))
colubrisCN1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 17))
colubrisCN1250 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 18))
colubrisCN320SE = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 19))
colubrisCN320 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 20))
colubrisCN1220 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 21))
colubrisCN200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 22))
colubrisCN3300 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 23))
colubrisCN330 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 24))
colubrisMSC5200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 25))
colubrisWCB200 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 26))
colubrisMSC5500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 27))
colubrisMAP625 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 28))
colubrisMAP630 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 29))
colubrisMAP330SENSOR = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 32))
colubris1300 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 33))
colubris1500 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 34))
colubrisMSC5100 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 35))
colubrisMSM410 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 41))
colubrisMSM317 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 42))
colubrisMSM310R = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 43))
colubrisMSM320R = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 44))
colubrisMSM313R = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 45))
colubrisMSM323R = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 46))
colubrisMSM765 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 47))
colubrisMSM760 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 48))
colubrisMSM318 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 49))
colubrisMSM460 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 52))
colubrisMSM430 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 54))
colubrisMSM466 = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 55))
colubrisRFManager = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 1, 1000))
mibBuilder.exportSymbols("COLUBRIS-PRODUCTS-MIB", colubrisCN1000HEREUARE=colubrisCN1000HEREUARE, colubrisCN1150=colubrisCN1150, colubrisCN3300=colubrisCN3300, colubrisCN320SE=colubrisCN320SE, colubrisMSM313R=colubrisMSM313R, colubrisMSC5500=colubrisMSC5500, colubrisMSM317=colubrisMSM317, colubrisCN1000=colubrisCN1000, colubrisCN320=colubrisCN320, colubrisCN330=colubrisCN330, colubrisMSM460=colubrisMSM460, colubrisRFManager=colubrisRFManager, colubrisCN3200=colubrisCN3200, colubrisMSM323R=colubrisMSM323R, colubrisMSM318=colubrisMSM318, colubrisMSC5100=colubrisMSC5100, colubrisCN1220=colubrisCN1220, colubrisCN1200=colubrisCN1200, colubrisProductsMIB=colubrisProductsMIB, colubrisMSM310R=colubrisMSM310R, colubris1300=colubris1300, colubrisMSM410=colubrisMSM410, colubrisCN1250=colubrisCN1250, colubrisCN3100=colubrisCN3100, colubrisCN1050=colubrisCN1050, colubrisMSM760=colubrisMSM760, colubrisCN300=colubrisCN300, PYSNMP_MODULE_ID=colubrisProductsMIB, colubrisCN3000=colubrisCN3000, colubrisCN3500=colubrisCN3500, colubrisCN310=colubrisCN310, colubrisCN1550=colubrisCN1550, colubrisMSC5200=colubrisMSC5200, colubrisCN100HEREUARE=colubrisCN100HEREUARE, colubrisWCB200=colubrisWCB200, colubrisMAP330SENSOR=colubrisMAP330SENSOR, colubrisCN200=colubrisCN200, colubrisMSM430=colubrisMSM430, colubrisMSM320R=colubrisMSM320R, colubrisCN100TRAVELNET=colubrisCN100TRAVELNET, colubrisMSM765=colubrisMSM765, colubrisMSM466=colubrisMSM466, colubris1500=colubris1500, colubrisCN1000LIGHT=colubrisCN1000LIGHT, colubrisCN1500=colubrisCN1500, colubrisCN1054=colubrisCN1054, colubrisMAP625=colubrisMAP625, colubrisMAP630=colubrisMAP630)
