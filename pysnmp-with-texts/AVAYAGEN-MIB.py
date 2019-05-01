#
# PySNMP MIB module AVAYAGEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVAYAGEN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:32:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Gauge32, Counter64, IpAddress, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Unsigned32, ObjectIdentity, enterprises, Integer32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Counter64", "IpAddress", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Unsigned32", "ObjectIdentity", "enterprises", "Integer32", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
avaya = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889))
avaya.setRevisions(('1909-12-19 10:00', '1904-01-27 09:00', '1902-08-15 09:00', '1902-07-28 09:00', '1901-08-09 17:00', '1901-06-21 11:55', '1900-10-15 10:45', '1900-10-15 13:05',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: avaya.setRevisionsDescriptions(('Rev 1.4.1 - Nick Saparoff. rename mibs to avayaMibs. rename products to avayaProducts. ', 'Rev 1.4.0 - Meir Deutsch. adds avGatewayProducts under avayaProducts. adds avGatewayMibs under avayaMibs. ', 'Rev 1.3.0 - Itai Zilbershterin. adds avayaSystemStats under lsg. ', 'Rev 1.2.0 - Itai Zilbershterin. adds avayaEISTopology under lsg. ', 'Rev 1.1.0 - Itai Zilbershterin. adds products OID to those defined. ', 'Rev 1.0.0 - Itai Zilbershterin. Fixed the mibs placement error. Avaya Mibs reside under avaya.2 and not avaya.1. The MIB branch is called avayaMibs.', 'Rev 0.9.0 - Itai Zilbershterin. The initial version of this MIB module. The following Organizational top-level groups are defined: lsg - Mibs of the LAN System Group (Concord & Israel).', "Rev 0.9.1 - Itai Zilbershterin. Dates in Revisions changed from 'yyyymmddhhmm' to 'yymmddhhmm', to support older development environments.",))
if mibBuilder.loadTexts: avaya.setLastUpdated('0401270900Z')
if mibBuilder.loadTexts: avaya.setOrganization('Avaya Inc.')
if mibBuilder.loadTexts: avaya.setContactInfo('Avaya Customer Services Postal: Avaya, Inc. 211 Mt Airy Rd. Basking Ridge, NJ 07920 USA Tel: +1 908 953 6000 WWW: http://www.avaya.com ')
if mibBuilder.loadTexts: avaya.setDescription('Avaya top-level OID tree. This MIB module deals defines the Avaya enterprise-specific tree. Development organizations within Avaya who wish to register MIBs under the Avaya enterprise OID, should: a. Contact the maintainer of this module, and get an organization OID and group OID. b. Import the definition of their Organization OID from this MIB. ')
avayaProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1))
avayaMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2))
avGatewayProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 6))
avGatewayMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6))
lsg = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1))
avayaEISTopology = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 10))
avayaSystemStats = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 11))
mibBuilder.exportSymbols("AVAYAGEN-MIB", avayaMibs=avayaMibs, avayaEISTopology=avayaEISTopology, avGatewayMibs=avGatewayMibs, lsg=lsg, avayaProducts=avayaProducts, avayaSystemStats=avayaSystemStats, PYSNMP_MODULE_ID=avaya, avGatewayProducts=avGatewayProducts, avaya=avaya)
