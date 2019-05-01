#
# PySNMP MIB module TIARA-NETWORKS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-NETWORKS-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Gauge32, TimeTicks, Counter32, Unsigned32, ObjectIdentity, Integer32, ModuleIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "TimeTicks", "Counter32", "Unsigned32", "ObjectIdentity", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tiaraModules, tiaraProducts = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraModules", "tiaraProducts")
tiaraProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 3, 1))
tiaraProductsMIB.setRevisions(('1999-04-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tiaraProductsMIB.setRevisionsDescriptions(('Initial version of the module.',))
if mibBuilder.loadTexts: tiaraProductsMIB.setLastUpdated('9904230000Z')
if mibBuilder.loadTexts: tiaraProductsMIB.setOrganization('Tiara Networks, Inc.')
if mibBuilder.loadTexts: tiaraProductsMIB.setContactInfo(' Tiara Networks Customer Service Postal: 525 Race Street, Suite 100, San Jose, CA 95126 USA Tel: +1 408-216-4700 Fax: +1 408-216-4701 E-mail: support@tiaranetworks.com')
if mibBuilder.loadTexts: tiaraProductsMIB.setDescription('This module defines the object identifiers that are assigned to various hardware platforms, and hence are returned as values for sysObjectID')
tiara1400 = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 1, 1))
tiara6100 = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 1, 2))
tiara6200 = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 1, 3))
tiara6300 = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 1, 4))
tiara1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 1, 5))
tiara1250 = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 1, 6))
tiara1450 = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 1, 7))
tiara7011 = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 1, 8))
tiara7030 = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 1, 9))
tiara7050 = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 1, 10))
tiara4100 = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 1, 11))
mibBuilder.exportSymbols("TIARA-NETWORKS-PRODUCTS-MIB", tiara1400=tiara1400, tiara6100=tiara6100, tiara1250=tiara1250, tiara1450=tiara1450, tiara7011=tiara7011, tiara4100=tiara4100, tiara7030=tiara7030, tiara7050=tiara7050, tiara6300=tiara6300, tiaraProductsMIB=tiaraProductsMIB, tiara6200=tiara6200, tiara1200=tiara1200, PYSNMP_MODULE_ID=tiaraProductsMIB)
