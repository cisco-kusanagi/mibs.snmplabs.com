#
# PySNMP MIB module TC-GROUPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TC-GROUPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:15:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, ObjectIdentity, Integer32, ModuleIdentity, enterprises, NotificationType, IpAddress, TimeTicks, Unsigned32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "ObjectIdentity", "Integer32", "ModuleIdentity", "enterprises", "NotificationType", "IpAddress", "TimeTicks", "Unsigned32", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbTcGroups = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10))
nbTcGroups.setRevisions(('2006-01-12 00:00', '2005-07-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nbTcGroups.setRevisionsDescriptions(("1. nbTcGrpSupport has been added. 2. nbTcActCtrlTable & nbTcActReslTable 3. 'smilib' tested.", 'Initial edition.',))
if mibBuilder.loadTexts: nbTcGroups.setLastUpdated('200601120000Z')
if mibBuilder.loadTexts: nbTcGroups.setOrganization('MRV Communications, Inc.')
if mibBuilder.loadTexts: nbTcGroups.setContactInfo('Alex Rozin MRV Communication, Inc http://www.mrv.com Email: ARozin@mrv.com')
if mibBuilder.loadTexts: nbTcGroups.setDescription('Traffic Conditioner Counters management.')
nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 629))
nbSwitchG1 = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1))
nbSwitchG1Il = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50))
nbRouterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 12))
nbRtActionLists = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9))
nbTcGrpSupport = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 100))
nbTcGrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101))
class SupportValue(TextualConvention, Integer32):
    description = 'Represents a value, that reflects support of the feature on the Device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("notSupported", 1), ("supported", 2))

class EntryValidator(TextualConvention, Integer32):
    description = 'Status for controlling of the entry.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("valid", 1), ("invalid", 2))

nbTcGrpCntrTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 1), )
if mibBuilder.loadTexts: nbTcGrpCntrTable.setStatus('current')
if mibBuilder.loadTexts: nbTcGrpCntrTable.setDescription('Control table for create/delete entries.')
nbTcGrpCntrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 1, 1), ).setIndexNames((0, "TC-GROUPS-MIB", "nbTcGroupCntrGrpName"), (0, "TC-GROUPS-MIB", "nbTcGroupCntrActionName"))
if mibBuilder.loadTexts: nbTcGrpCntrEntry.setStatus('current')
if mibBuilder.loadTexts: nbTcGrpCntrEntry.setDescription('.')
nbTcGroupCntrGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: nbTcGroupCntrGrpName.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupCntrGrpName.setDescription('The human readable name for a group of TC counters.')
nbTcGroupCntrActionName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: nbTcGroupCntrActionName.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupCntrActionName.setDescription('The human readable name for an action list.')
nbTcGroupCntrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 1, 1, 3), EntryValidator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbTcGroupCntrStatus.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupCntrStatus.setDescription('Status for controlling of the entry.')
nbTcGrpDscrTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 2), )
if mibBuilder.loadTexts: nbTcGrpDscrTable.setStatus('current')
if mibBuilder.loadTexts: nbTcGrpDscrTable.setDescription('Table to manage (set/delete/obtain) descriptions of groups.')
nbTcGrpDscrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 2, 1), ).setIndexNames((0, "TC-GROUPS-MIB", "nbTcGroupDscrGrpName"))
if mibBuilder.loadTexts: nbTcGrpDscrEntry.setStatus('current')
if mibBuilder.loadTexts: nbTcGrpDscrEntry.setDescription('.')
nbTcGroupDscrGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: nbTcGroupDscrGrpName.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupDscrGrpName.setDescription('The human readable name for a group of TC counters.')
nbTcGroupDscrText = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbTcGroupDscrText.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupDscrText.setDescription('Description of the group.')
nbTcGrpReslTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3), )
if mibBuilder.loadTexts: nbTcGrpReslTable.setStatus('current')
if mibBuilder.loadTexts: nbTcGrpReslTable.setDescription('Counters and statuses of entries.')
nbTcGrpReslEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1), )
nbTcGrpCntrEntry.registerAugmentions(("TC-GROUPS-MIB", "nbTcGrpReslEntry"))
nbTcGrpReslEntry.setIndexNames(*nbTcGrpCntrEntry.getIndexNames())
if mibBuilder.loadTexts: nbTcGrpReslEntry.setStatus('current')
if mibBuilder.loadTexts: nbTcGrpReslEntry.setDescription('.')
nbTcGroupReslStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslStatus.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslStatus.setDescription('Current status of the action list.')
nbTcGroupReslCnfrmncCntrSet = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslCnfrmncCntrSet.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslCnfrmncCntrSet.setDescription("Number of 'Conformance Counter Set'; value '0' means, that there is no assigned 'Conformance Counter Set'.")
nbTcGroupReslMeteringGreens = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslMeteringGreens.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslMeteringGreens.setDescription('Metering bytes with green conformance.')
nbTcGroupReslMeteringYellows = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslMeteringYellows.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslMeteringYellows.setDescription('Metering bytes with yellow conformance.')
nbTcGroupReslMeteringReds = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslMeteringReds.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslMeteringReds.setDescription('Metering bytes with red conformance.')
nbTcGroupReslAggrOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslAggrOctets.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslAggrOctets.setDescription('Admitted bytes for flow aggregate.')
nbTcGroupReslAggrPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslAggrPackets.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslAggrPackets.setDescription('Admitted packets for flow aggregate.')
nbTcGroupReslConfGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslConfGreenOctets.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslConfGreenOctets.setDescription("Number of bytes marked green in selected 'Conformance Counter Set'.")
nbTcGroupReslConfGreenPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslConfGreenPackets.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslConfGreenPackets.setDescription("Number of packets marked green in selected 'Conformance Counter Set'.")
nbTcGroupReslConfYellowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslConfYellowOctets.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslConfYellowOctets.setDescription("Number of bytes marked yellow in selected 'Conformance Counter Set'.")
nbTcGroupReslConfYellowPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslConfYellowPackets.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslConfYellowPackets.setDescription("Number of packets marked yellow in selected 'Conformance Counter Set'.")
nbTcGroupReslConfRedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslConfRedOctets.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslConfRedOctets.setDescription("Number of bytes marked red in selected 'Conformance Counter Set'.")
nbTcGroupReslConfRedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGroupReslConfRedPackets.setStatus('current')
if mibBuilder.loadTexts: nbTcGroupReslConfRedPackets.setDescription("Number of packets marked red in selected 'Conformance Counter Set'.")
nbTcActCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 9), )
if mibBuilder.loadTexts: nbTcActCtrlTable.setStatus('current')
if mibBuilder.loadTexts: nbTcActCtrlTable.setDescription('Control table for create/delete entries.')
nbTcActCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 9, 1), ).setIndexNames((0, "TC-GROUPS-MIB", "nbTcActName"))
if mibBuilder.loadTexts: nbTcActCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: nbTcActCtrlEntry.setDescription('.')
nbTcActName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 9, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: nbTcActName.setStatus('current')
if mibBuilder.loadTexts: nbTcActName.setDescription('The human readable name for a Action List.')
nbTcActStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 9, 1, 64), EntryValidator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbTcActStatus.setStatus('current')
if mibBuilder.loadTexts: nbTcActStatus.setDescription('Status for controlling of the entry.')
nbTcActReslTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 10), )
if mibBuilder.loadTexts: nbTcActReslTable.setStatus('current')
if mibBuilder.loadTexts: nbTcActReslTable.setDescription('Control table for create/delete entries.')
nbTcActReslEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 10, 1), )
nbTcActCtrlEntry.registerAugmentions(("TC-GROUPS-MIB", "nbTcActReslEntry"))
nbTcActReslEntry.setIndexNames(*nbTcActCtrlEntry.getIndexNames())
if mibBuilder.loadTexts: nbTcActReslEntry.setStatus('current')
if mibBuilder.loadTexts: nbTcActReslEntry.setDescription('.')
nbTcActReslStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 10, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcActReslStatus.setStatus('current')
if mibBuilder.loadTexts: nbTcActReslStatus.setDescription('Current status of the action list.')
nbTcGrpSupportGroups = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 100, 2), SupportValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGrpSupportGroups.setStatus('current')
if mibBuilder.loadTexts: nbTcGrpSupportGroups.setDescription('The device supports nbTcGrpCntrTable, nbTcGrpDscrTable & nbTcGrpReslTable.')
nbTcGrpSupportLists = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 100, 9), SupportValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbTcGrpSupportLists.setStatus('current')
if mibBuilder.loadTexts: nbTcGrpSupportLists.setDescription('The device supports nbTcActCtrlTable & nbTcActReslTable.')
nbTcGrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 1))
nbTcGrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 2))
nbTcGrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 1, 1)).setObjects(("TC-GROUPS-MIB", "nbTcGrpSupportReflectors"), ("TC-GROUPS-MIB", "nbTcGrpGroup"), ("TC-GROUPS-MIB", "nbTcActGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nbTcGrpMIBCompliance = nbTcGrpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: nbTcGrpMIBCompliance.setDescription('The core compliance statement for all nbTcGer MIB implementations.')
nbTcGrpSupportReflectors = ObjectGroup((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 2, 1)).setObjects(("TC-GROUPS-MIB", "nbTcGrpSupportGroups"), ("TC-GROUPS-MIB", "nbTcGrpSupportLists"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nbTcGrpSupportReflectors = nbTcGrpSupportReflectors.setStatus('current')
if mibBuilder.loadTexts: nbTcGrpSupportReflectors.setDescription('Mandatory Conformance group : represents a value, that reflects support of the feature on the Device.')
nbTcGrpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 2, 2)).setObjects(("TC-GROUPS-MIB", "nbTcGroupCntrStatus"), ("TC-GROUPS-MIB", "nbTcGroupDscrText"), ("TC-GROUPS-MIB", "nbTcGroupReslStatus"), ("TC-GROUPS-MIB", "nbTcGroupReslCnfrmncCntrSet"), ("TC-GROUPS-MIB", "nbTcGroupReslMeteringGreens"), ("TC-GROUPS-MIB", "nbTcGroupReslMeteringYellows"), ("TC-GROUPS-MIB", "nbTcGroupReslMeteringReds"), ("TC-GROUPS-MIB", "nbTcGroupReslAggrOctets"), ("TC-GROUPS-MIB", "nbTcGroupReslAggrPackets"), ("TC-GROUPS-MIB", "nbTcGroupReslConfGreenOctets"), ("TC-GROUPS-MIB", "nbTcGroupReslConfGreenPackets"), ("TC-GROUPS-MIB", "nbTcGroupReslConfYellowOctets"), ("TC-GROUPS-MIB", "nbTcGroupReslConfYellowPackets"), ("TC-GROUPS-MIB", "nbTcGroupReslConfRedOctets"), ("TC-GROUPS-MIB", "nbTcGroupReslConfRedPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nbTcGrpGroup = nbTcGrpGroup.setStatus('current')
if mibBuilder.loadTexts: nbTcGrpGroup.setDescription('Optional objects for grouping of Action Lists TC counters.')
nbTcActGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 629, 1, 50, 12, 9, 10, 101, 2, 3)).setObjects(("TC-GROUPS-MIB", "nbTcActStatus"), ("TC-GROUPS-MIB", "nbTcActReslStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nbTcActGroup = nbTcActGroup.setStatus('current')
if mibBuilder.loadTexts: nbTcActGroup.setDescription('Optional objects, Action List without grouping.')
mibBuilder.exportSymbols("TC-GROUPS-MIB", nbTcActName=nbTcActName, nbTcGroupReslAggrPackets=nbTcGroupReslAggrPackets, nbTcActReslStatus=nbTcActReslStatus, nbTcGrpDscrEntry=nbTcGrpDscrEntry, nbTcGroupReslAggrOctets=nbTcGroupReslAggrOctets, nbTcActReslTable=nbTcActReslTable, nbTcGroupReslMeteringGreens=nbTcGroupReslMeteringGreens, SupportValue=SupportValue, nbTcGrpCntrTable=nbTcGrpCntrTable, nbTcGrpReslTable=nbTcGrpReslTable, nbTcGroupDscrText=nbTcGroupDscrText, nbTcGrpSupport=nbTcGrpSupport, nbTcGroupReslConfGreenOctets=nbTcGroupReslConfGreenOctets, nbTcGroupReslConfRedOctets=nbTcGroupReslConfRedOctets, nbTcGrpConformance=nbTcGrpConformance, nbTcGroupReslMeteringYellows=nbTcGroupReslMeteringYellows, nbase=nbase, nbTcGroupReslConfGreenPackets=nbTcGroupReslConfGreenPackets, nbTcActStatus=nbTcActStatus, nbTcActGroup=nbTcActGroup, PYSNMP_MODULE_ID=nbTcGroups, nbTcGroupReslConfYellowPackets=nbTcGroupReslConfYellowPackets, nbTcActCtrlTable=nbTcActCtrlTable, nbSwitchG1Il=nbSwitchG1Il, EntryValidator=EntryValidator, nbTcGroupReslConfRedPackets=nbTcGroupReslConfRedPackets, nbTcGroups=nbTcGroups, nbRouterConfig=nbRouterConfig, nbTcGrpGroup=nbTcGrpGroup, nbTcGrpSupportLists=nbTcGrpSupportLists, nbRtActionLists=nbRtActionLists, nbTcGroupReslConfYellowOctets=nbTcGroupReslConfYellowOctets, nbTcGrpMIBCompliance=nbTcGrpMIBCompliance, nbTcGroupReslMeteringReds=nbTcGroupReslMeteringReds, nbTcGrpMIBCompliances=nbTcGrpMIBCompliances, nbSwitchG1=nbSwitchG1, nbTcGroupReslCnfrmncCntrSet=nbTcGroupReslCnfrmncCntrSet, nbTcActCtrlEntry=nbTcActCtrlEntry, nbTcGrpSupportReflectors=nbTcGrpSupportReflectors, nbTcGrpCntrEntry=nbTcGrpCntrEntry, nbTcGrpSupportGroups=nbTcGrpSupportGroups, nbTcGroupCntrStatus=nbTcGroupCntrStatus, nbTcGrpMIBGroups=nbTcGrpMIBGroups, nbTcGroupDscrGrpName=nbTcGroupDscrGrpName, nbTcGroupCntrGrpName=nbTcGroupCntrGrpName, nbTcGroupCntrActionName=nbTcGroupCntrActionName, nbTcActReslEntry=nbTcActReslEntry, nbTcGrpDscrTable=nbTcGrpDscrTable, nbTcGrpReslEntry=nbTcGrpReslEntry, nbTcGroupReslStatus=nbTcGroupReslStatus)
