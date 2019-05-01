#
# PySNMP MIB module JUNIPER-HOSTRESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-HOSTRESOURCES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hrStorageEntry, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrStorageEntry")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, Integer32, iso, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, ModuleIdentity, ObjectIdentity, MibIdentifier, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Integer32", "iso", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxHostResourcesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 31))
jnxHostResourcesMIB.setRevisions(('2004-08-18 00:00', '2004-05-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxHostResourcesMIB.setRevisionsDescriptions(('Fixed typo in description clauses.', 'Initial revision.',))
if mibBuilder.loadTexts: jnxHostResourcesMIB.setLastUpdated('200408180000Z')
if mibBuilder.loadTexts: jnxHostResourcesMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxHostResourcesMIB.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxHostResourcesMIB.setDescription('Extends the HOST-RESOURCES-MIB (rfc2790).')
jnxHrStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1))
jnxHrStorageTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1), )
if mibBuilder.loadTexts: jnxHrStorageTable.setStatus('current')
if mibBuilder.loadTexts: jnxHrStorageTable.setDescription('Augments the hrStorageTable with additional data.')
jnxHrStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1), )
hrStorageEntry.registerAugmentions(("JUNIPER-HOSTRESOURCES-MIB", "jnxHrStorageEntry"))
jnxHrStorageEntry.setIndexNames(*hrStorageEntry.getIndexNames())
if mibBuilder.loadTexts: jnxHrStorageEntry.setStatus('current')
if mibBuilder.loadTexts: jnxHrStorageEntry.setDescription('Each entry provides additional file system data beyond that available in the hrStorageTable.')
jnxHrStoragePercentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 31, 1, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxHrStoragePercentUsed.setStatus('current')
if mibBuilder.loadTexts: jnxHrStoragePercentUsed.setDescription('The amount of the storage represented by this entry that is allocated, as a percentage of the total amount available.')
mibBuilder.exportSymbols("JUNIPER-HOSTRESOURCES-MIB", jnxHrStorageEntry=jnxHrStorageEntry, jnxHrStoragePercentUsed=jnxHrStoragePercentUsed, jnxHostResourcesMIB=jnxHostResourcesMIB, jnxHrStorage=jnxHrStorage, jnxHrStorageTable=jnxHrStorageTable, PYSNMP_MODULE_ID=jnxHostResourcesMIB)
