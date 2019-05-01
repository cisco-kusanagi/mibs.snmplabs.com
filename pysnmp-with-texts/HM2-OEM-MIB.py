#
# PySNMP MIB module HM2-OEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-OEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:31:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hm2ConfigurationMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, Integer32, Counter64, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ModuleIdentity, Counter32, NotificationType, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Integer32", "Counter64", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "ModuleIdentity", "Counter32", "NotificationType", "IpAddress", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hm2OemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 15))
hm2OemMib.setRevisions(('2011-03-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hm2OemMib.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hm2OemMib.setLastUpdated('201103310000Z')
if mibBuilder.loadTexts: hm2OemMib.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hm2OemMib.setContactInfo('Postal: Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Phone: +49 7127 140 E-mail: hac.support@belden.com')
if mibBuilder.loadTexts: hm2OemMib.setDescription('Hirschmann OEM MIB. Copyright (C) 2011. All Rights Reserved.')
hm2OemMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 15, 1))
hm2OemID = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2OemID.setStatus('current')
if mibBuilder.loadTexts: hm2OemID.setDescription('Unique OEM ID.')
mibBuilder.exportSymbols("HM2-OEM-MIB", hm2OemID=hm2OemID, hm2OemMibObjects=hm2OemMibObjects, hm2OemMib=hm2OemMib, PYSNMP_MODULE_ID=hm2OemMib)
