#
# PySNMP MIB module HM2-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:32:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
hm2ConfigurationMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Counter64, MibIdentifier, TimeTicks, ObjectIdentity, Counter32, NotificationType, Gauge32, iso, Integer32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Counter64", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Counter32", "NotificationType", "Gauge32", "iso", "Integer32", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hm2QosMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 32))
hm2QosMib.setRevisions(('2011-03-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hm2QosMib.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hm2QosMib.setLastUpdated('201103160000Z')
if mibBuilder.loadTexts: hm2QosMib.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hm2QosMib.setContactInfo('Postal: Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Phone: +49 7127 140 E-mail: hac.support@belden.com')
if mibBuilder.loadTexts: hm2QosMib.setDescription('Hirschmann Quality of Service MIB. Copyright (C) 2011. All Rights Reserved.')
hm2QosMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 0))
hm2QosMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1))
hm2QosFirstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1, 1))
hm2QosNextGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1, 2))
mibBuilder.exportSymbols("HM2-QOS-MIB", hm2QosMibNotifications=hm2QosMibNotifications, hm2QosMibObjects=hm2QosMibObjects, hm2QosMib=hm2QosMib, hm2QosFirstGroup=hm2QosFirstGroup, PYSNMP_MODULE_ID=hm2QosMib, hm2QosNextGroup=hm2QosNextGroup)
