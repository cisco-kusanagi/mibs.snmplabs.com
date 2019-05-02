#
# PySNMP MIB module CISCO-PRODUCTS-MIB-CORRECTIONS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PRODUCTS-MIB-CORRECTIONS
# Produced by pysmi-0.3.4 at Wed May  1 12:10:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoModules, ciscoProducts = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules", "ciscoProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Counter32, Unsigned32, MibIdentifier, NotificationType, ModuleIdentity, Integer32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Counter32", "Unsigned32", "MibIdentifier", "NotificationType", "ModuleIdentity", "Integer32", "Counter64", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoProductsMIBCorrections = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 65535))
ciscoProductsMIBCorrections.setRevisions(('2014-11-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setRevisionsDescriptions((' Initial version for the netdisco-mibs distribution. Added OIDs for the Catalyst 3650 platform. ',))
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setLastUpdated('201411270000Z')
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setOrganization('The Netdisco project')
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setContactInfo(' Mailing list: netdisco-users@lists.sourceforge.net IRC: #netdisco on Freenode ')
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setDescription(' This module augments the CISCO-PRODUCTS-MIB. It defines additional object identifiers that are assigned to various hardware platforms, and hence are returned as values for sysObjectID. ')
catalyst365024TS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1823))
catalyst365048TS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1824))
catalyst365024PS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1825))
catalyst365048PS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1826))
catalyst365024TD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1827))
catalyst365048TD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1828))
catalyst365024PD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1829))
catalyst365048PD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1830))
mibBuilder.exportSymbols("CISCO-PRODUCTS-MIB-CORRECTIONS", catalyst365048TD=catalyst365048TD, catalyst365024TD=catalyst365024TD, ciscoProductsMIBCorrections=ciscoProductsMIBCorrections, catalyst365048PD=catalyst365048PD, PYSNMP_MODULE_ID=ciscoProductsMIBCorrections, catalyst365024PS=catalyst365024PS, catalyst365048PS=catalyst365048PS, catalyst365048TS=catalyst365048TS, catalyst365024TS=catalyst365024TS, catalyst365024PD=catalyst365024PD)
