#
# PySNMP MIB module JUNIPER-FRU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-FRU-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
jnxFruTraps, jnxFruMibRoot = mibBuilder.importSymbols("JUNIPER-SMI", "jnxFruTraps", "jnxFruMibRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, TimeTicks, Integer32, iso, Gauge32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "TimeTicks", "Integer32", "iso", "Gauge32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxFruMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1))
jnxFruMib.setRevisions(('2012-01-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxFruMib.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: jnxFruMib.setLastUpdated('201211131414Z')
if mibBuilder.loadTexts: jnxFruMib.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxFruMib.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxFruMib.setDescription("This MIB module defines objects used for managing the OTN FRU's for Juniper products.")
class JnxFruAdminStates(TextualConvention, Integer32):
    description = 'Admin states for a FRU'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2))

class JnxFruOperStates(TextualConvention, Integer32):
    description = 'Operation states for a FRU'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unEquipped", 1), ("init", 2), ("normal", 3), ("mismatched", 4), ("fault", 5), ("swul", 6))

jnxFruCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1))
jnxFruCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1), )
if mibBuilder.loadTexts: jnxFruCfgTable.setStatus('current')
if mibBuilder.loadTexts: jnxFruCfgTable.setDescription("Information about the otn FRU's. ")
jnxFruCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1), ).setIndexNames((0, "JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"), (0, "JUNIPER-FRU-MIB", "jnxFruCfgL1Index"), (0, "JUNIPER-FRU-MIB", "jnxFruCfgL2Index"), (0, "JUNIPER-FRU-MIB", "jnxFruCfgL3Index"))
if mibBuilder.loadTexts: jnxFruCfgEntry.setStatus('current')
if mibBuilder.loadTexts: jnxFruCfgEntry.setDescription("Information about the otn FRU's.")
jnxFruCfgContentsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxFruCfgContentsIndex.setStatus('current')
if mibBuilder.loadTexts: jnxFruCfgContentsIndex.setDescription('The associated jnxContentsContainerIndex in the jnxContentsTable.')
jnxFruCfgL1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxFruCfgL1Index.setStatus('current')
if mibBuilder.loadTexts: jnxFruCfgL1Index.setDescription('The level one index associated with this subject. Zero if unavailable or inapplicable.')
jnxFruCfgL2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxFruCfgL2Index.setStatus('current')
if mibBuilder.loadTexts: jnxFruCfgL2Index.setDescription('The level two index associated with this subject. Zero if unavailable or inapplicable.')
jnxFruCfgL3Index = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxFruCfgL3Index.setStatus('current')
if mibBuilder.loadTexts: jnxFruCfgL3Index.setDescription('The level three index associated with this subject. Zero if unavailable or inapplicable.')
jnxFruCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 5), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jnxFruCfgType.setStatus('current')
if mibBuilder.loadTexts: jnxFruCfgType.setDescription('The object ID for this FRU')
jnxFruCfgAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 6), JnxFruAdminStates()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jnxFruCfgAdminState.setStatus('current')
if mibBuilder.loadTexts: jnxFruCfgAdminState.setDescription('The Administrative state of this FRU')
jnxFruCfgOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 7), JnxFruOperStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFruCfgOperState.setStatus('current')
if mibBuilder.loadTexts: jnxFruCfgOperState.setDescription('The Operational state of this FRU')
jnxFruNotifMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 23, 1)).setObjects(("JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"), ("JUNIPER-FRU-MIB", "jnxFruCfgL1Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL2Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL3Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgType"))
if mibBuilder.loadTexts: jnxFruNotifMismatch.setStatus('current')
if mibBuilder.loadTexts: jnxFruNotifMismatch.setDescription('A jnxFruInsertion trap signifies that the SNMP entity, acting in an agent role, has detected that the specified FRU (Field Replaceable Unit) inserted into the chassis does not match what was configured.')
jnxFruNotifAdminStatus = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 23, 2)).setObjects(("JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"), ("JUNIPER-FRU-MIB", "jnxFruCfgL1Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL2Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL3Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgAdminState"))
if mibBuilder.loadTexts: jnxFruNotifAdminStatus.setStatus('current')
if mibBuilder.loadTexts: jnxFruNotifAdminStatus.setDescription('Notification of the Administrative state of the otn interface')
jnxFruNotifOperStatus = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 23, 3)).setObjects(("JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"), ("JUNIPER-FRU-MIB", "jnxFruCfgL1Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL2Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgL3Index"), ("JUNIPER-FRU-MIB", "jnxFruCfgOperState"))
if mibBuilder.loadTexts: jnxFruNotifOperStatus.setStatus('current')
if mibBuilder.loadTexts: jnxFruNotifOperStatus.setDescription('Notification of Operational state of the otn interface')
mibBuilder.exportSymbols("JUNIPER-FRU-MIB", JnxFruAdminStates=JnxFruAdminStates, jnxFruCfgContentsIndex=jnxFruCfgContentsIndex, PYSNMP_MODULE_ID=jnxFruMib, jnxFruCfgTable=jnxFruCfgTable, jnxFruCfgL3Index=jnxFruCfgL3Index, jnxFruCfgL2Index=jnxFruCfgL2Index, jnxFruCfgOperState=jnxFruCfgOperState, jnxFruCfg=jnxFruCfg, JnxFruOperStates=JnxFruOperStates, jnxFruCfgL1Index=jnxFruCfgL1Index, jnxFruMib=jnxFruMib, jnxFruCfgEntry=jnxFruCfgEntry, jnxFruNotifAdminStatus=jnxFruNotifAdminStatus, jnxFruNotifOperStatus=jnxFruNotifOperStatus, jnxFruCfgAdminState=jnxFruCfgAdminState, jnxFruNotifMismatch=jnxFruNotifMismatch, jnxFruCfgType=jnxFruCfgType)
