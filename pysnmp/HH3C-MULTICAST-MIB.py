#
# PySNMP MIB module HH3C-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, ModuleIdentity, iso, Bits, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, Gauge32, Integer32, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "ModuleIdentity", "iso", "Bits", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "Gauge32", "Integer32", "Unsigned32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cMulticast = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 50))
hh3cMulticast.setRevisions(('2005-04-29 00:00',))
if mibBuilder.loadTexts: hh3cMulticast.setLastUpdated('200504290000Z')
if mibBuilder.loadTexts: hh3cMulticast.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hh3cMulticastObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 50, 1))
hh3cMulticastEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 50, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMulticastEnable.setStatus('current')
mibBuilder.exportSymbols("HH3C-MULTICAST-MIB", hh3cMulticast=hh3cMulticast, hh3cMulticastObject=hh3cMulticastObject, PYSNMP_MODULE_ID=hh3cMulticast, hh3cMulticastEnable=hh3cMulticastEnable, EnabledStatus=EnabledStatus)
