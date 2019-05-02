#
# PySNMP MIB module NET-SNMP-VACM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NET-SNMP-VACM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:18:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
netSnmpObjects, netSnmpGroups = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpObjects", "netSnmpGroups")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
vacmAccessContextPrefix, vacmAccessSecurityLevel, vacmAccessSecurityModel, vacmGroupName = mibBuilder.importSymbols("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessContextPrefix", "vacmAccessSecurityLevel", "vacmAccessSecurityModel", "vacmGroupName")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, Counter32, ModuleIdentity, Integer32, TimeTicks, Counter64, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "ModuleIdentity", "Integer32", "TimeTicks", "Counter64", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Bits", "iso", "ObjectIdentity")
RowStatus, StorageType, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "DisplayString", "TextualConvention")
netSnmpVacmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 1, 9))
netSnmpVacmMIB.setRevisions(('2006-08-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netSnmpVacmMIB.setRevisionsDescriptions(('First draft',))
if mibBuilder.loadTexts: netSnmpVacmMIB.setLastUpdated('200608270000Z')
if mibBuilder.loadTexts: netSnmpVacmMIB.setOrganization('www.net-snmp.org')
if mibBuilder.loadTexts: netSnmpVacmMIB.setContactInfo('postal: Wes Hardaker P.O. Box 382 Davis CA 95617 email: net-snmp-coders@lists.sourceforge.net')
if mibBuilder.loadTexts: netSnmpVacmMIB.setDescription('Defines Net-SNMP extensions to the standard VACM view table.')
nsVacmAccessTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 9, 1), )
if mibBuilder.loadTexts: nsVacmAccessTable.setStatus('current')
if mibBuilder.loadTexts: nsVacmAccessTable.setDescription('Net-SNMP extensions to vacmAccessTable.')
nsVacmAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmGroupName"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessContextPrefix"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityModel"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityLevel"), (0, "NET-SNMP-VACM-MIB", "nsVacmAuthType"))
if mibBuilder.loadTexts: nsVacmAccessEntry.setStatus('current')
if mibBuilder.loadTexts: nsVacmAccessEntry.setDescription('Net-SNMP extensions to vacmAccessTable.')
nsVacmAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: nsVacmAuthType.setStatus('current')
if mibBuilder.loadTexts: nsVacmAuthType.setDescription("The type of processing that the specified view should be applied to. See 'snmpd.conf(5)' and 'snmptrapd.conf(5)' for details.")
nsVacmContextMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exact", 1), ("prefix", 2))).clone('exact')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsVacmContextMatch.setStatus('current')
if mibBuilder.loadTexts: nsVacmContextMatch.setDescription('If the value of this object is exact(1), then all rows where the contextName exactly matches vacmAccessContextPrefix are selected. If the value of this object is prefix(2), then all rows where the contextName whose starting octets exactly match vacmAccessContextPrefix are selected. This allows for a simple form of wildcarding. The value of this object should be consistent across all nsVacmAccessEntries corresponding to a single row of the vacmAccessTable. ')
nsVacmViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsVacmViewName.setStatus('current')
if mibBuilder.loadTexts: nsVacmViewName.setDescription('The MIB view authorised for the appropriate style of processing (as indicated by nsVacmToken). The interpretation of this value is the same as for the standard VACM ViewName objects.')
nsVacmStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsVacmStorageType.setStatus('current')
if mibBuilder.loadTexts: nsVacmStorageType.setDescription("The storage type for this (group of) conceptual rows. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row. The value of this object should be consistent across all nsVacmAccessEntries corresponding to a single row of the vacmAccessTable. ")
nsVacmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 9, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsVacmStatus.setStatus('current')
if mibBuilder.loadTexts: nsVacmStatus.setDescription('The status of this (group of) conceptual rows. The RowStatus TC [RFC2579] requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified: The value of this object has no effect on whether other objects in this conceptual row can be modified. The value of this object should be consistent across all nsVacmAccessEntries corresponding to a single row of the vacmAccessTable. ')
mibBuilder.exportSymbols("NET-SNMP-VACM-MIB", PYSNMP_MODULE_ID=netSnmpVacmMIB, netSnmpVacmMIB=netSnmpVacmMIB, nsVacmViewName=nsVacmViewName, nsVacmStorageType=nsVacmStorageType, nsVacmAccessEntry=nsVacmAccessEntry, nsVacmAuthType=nsVacmAuthType, nsVacmAccessTable=nsVacmAccessTable, nsVacmContextMatch=nsVacmContextMatch, nsVacmStatus=nsVacmStatus)
