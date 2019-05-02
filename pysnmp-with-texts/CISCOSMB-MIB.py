#
# PySNMP MIB module CISCOSMB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSMB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:24:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, MibIdentifier, TimeTicks, ObjectIdentity, Integer32, Bits, Unsigned32, Counter64, ModuleIdentity, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32", "Bits", "Unsigned32", "Counter64", "ModuleIdentity", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cisco = ModuleIdentity((1, 3, 6, 1, 4, 1, 9))
cisco.setRevisions(('2010-10-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cisco.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: cisco.setLastUpdated('201010310000Z')
if mibBuilder.loadTexts: cisco.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cisco.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: cisco.setDescription('The private MIB module definition for CISCOSB private MIB tree.')
otherEnterprises = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6))
ciscosb = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1))
switch001 = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101))
rndMib = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101))
mibBuilder.exportSymbols("CISCOSMB-MIB", PYSNMP_MODULE_ID=cisco, cisco=cisco, ciscosb=ciscosb, rndMib=rndMib, switch001=switch001, otherEnterprises=otherEnterprises)
