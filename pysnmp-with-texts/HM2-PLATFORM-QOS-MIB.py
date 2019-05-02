#
# PySNMP MIB module HM2-PLATFORM-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:32:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
hm2PlatformMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2PlatformMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Bits, ObjectIdentity, Counter32, NotificationType, Gauge32, Unsigned32, ModuleIdentity, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Bits", "ObjectIdentity", "Counter32", "NotificationType", "Gauge32", "Unsigned32", "ModuleIdentity", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2PlatformQoS = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 3))
hm2PlatformQoS.setRevisions(('2011-10-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hm2PlatformQoS.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hm2PlatformQoS.setLastUpdated('201110280000Z')
if mibBuilder.loadTexts: hm2PlatformQoS.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hm2PlatformQoS.setContactInfo('Postal: Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Phone: +49 7127 140 E-mail: hac.support@belden.com')
if mibBuilder.loadTexts: hm2PlatformQoS.setDescription('The Hirschmann Private Platform2 MIB for QoS. Copyright (C) 2011. All Rights Reserved.')
mibBuilder.exportSymbols("HM2-PLATFORM-QOS-MIB", PYSNMP_MODULE_ID=hm2PlatformQoS, hm2PlatformQoS=hm2PlatformQoS)
