#
# PySNMP MIB module JUNIPER-HOSTRESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-HOSTRESOURCES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
hrStorageEntry, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrStorageEntry")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, MibIdentifier, ModuleIdentity, Bits, Unsigned32, NotificationType, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibIdentifier", "ModuleIdentity", "Bits", "Unsigned32", "NotificationType", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxHostResourcesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 31))
jnxHostResourcesMIB.setRevisions(('2004-08-18 00:00', '2004-05-05 00:00',))
if mibBuilder.loadTexts: jnxHostResourcesMIB.setLastUpdated('200408180000Z')
if mibBuilder.loadTexts: jnxHostResourcesMIB.setOrganization('Juniper Networks, Inc.')
jnxHrStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1))
jnxHrStorageTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1), )
if mibBuilder.loadTexts: jnxHrStorageTable.setStatus('current')
jnxHrStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1), )
hrStorageEntry.registerAugmentions(("JUNIPER-HOSTRESOURCES-MIB", "jnxHrStorageEntry"))
jnxHrStorageEntry.setIndexNames(*hrStorageEntry.getIndexNames())
if mibBuilder.loadTexts: jnxHrStorageEntry.setStatus('current')
jnxHrStoragePercentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxHrStoragePercentUsed.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-HOSTRESOURCES-MIB", PYSNMP_MODULE_ID=jnxHostResourcesMIB, jnxHrStoragePercentUsed=jnxHrStoragePercentUsed, jnxHrStorageEntry=jnxHrStorageEntry, jnxHrStorageTable=jnxHrStorageTable, jnxHrStorage=jnxHrStorage, jnxHostResourcesMIB=jnxHostResourcesMIB)
