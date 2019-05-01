#
# PySNMP MIB module ARUBA-VENDORTYPE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARUBA-VENDORTYPE
# Produced by pysmi-0.3.4 at Wed May  1 11:25:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
arubaMIBModules, = mibBuilder.importSymbols("ARUBA-MIB", "arubaMIBModules")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, IpAddress, Counter64, ObjectIdentity, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "IpAddress", "Counter64", "ObjectIdentity", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arubaVendorTypeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1))
arubaVendorTypeMIB.setRevisions(('2012-08-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arubaVendorTypeMIB.setRevisionsDescriptions(('The initial revision of vendortype-oid MIB.',))
if mibBuilder.loadTexts: arubaVendorTypeMIB.setLastUpdated('201208270000Z')
if mibBuilder.loadTexts: arubaVendorTypeMIB.setOrganization('Aruba Wireless Networks')
if mibBuilder.loadTexts: arubaVendorTypeMIB.setContactInfo('Postal: 1322 Crossman Avenue Sunnyvale, CA 94089 E-mail: dl-support@arubanetworks.com Phone: +1 408 227 4500')
if mibBuilder.loadTexts: arubaVendorTypeMIB.setDescription('This module describes the object identifiers that are assigned to various components on aruba products.')
arubaVendorTypeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1))
arubaSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1))
aSystemUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 1))
aSystemChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 2))
aSystemBackplane = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 3))
aSystemModule = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 4))
aSystemPSU = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 5))
aSystemFAN = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 6))
aSystemContainer = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 7))
aSystemPort = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 8))
aSystemSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 1, 1, 1, 1, 1, 9))
mibBuilder.exportSymbols("ARUBA-VENDORTYPE", aSystemPort=aSystemPort, aSystemUnknown=aSystemUnknown, aSystemBackplane=aSystemBackplane, aSystemModule=aSystemModule, aSystemFAN=aSystemFAN, aSystemContainer=aSystemContainer, PYSNMP_MODULE_ID=arubaVendorTypeMIB, arubaVendorTypeMIB=arubaVendorTypeMIB, arubaVendorTypeMIBObjects=arubaVendorTypeMIBObjects, aSystemPSU=aSystemPSU, arubaSystem=arubaSystem, aSystemSensor=aSystemSensor, aSystemChassis=aSystemChassis)
