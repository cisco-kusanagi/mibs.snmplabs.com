#
# PySNMP MIB module CISCO-IF-LINK-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IF-LINK-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:01:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoLocationSpecifier, = mibBuilder.importSymbols("CISCO-TC", "CiscoLocationSpecifier")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, NotificationType, Bits, IpAddress, iso, ObjectIdentity, Integer32, Unsigned32, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "NotificationType", "Bits", "IpAddress", "iso", "ObjectIdentity", "Integer32", "Unsigned32", "Counter32", "MibIdentifier")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoIfLinkConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 175))
ciscoIfLinkConfigMIB.setRevisions(('2001-10-05 00:00', '2000-09-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setRevisionsDescriptions(('Add object cilTargetModuleFramingType in cilConfTable table', 'Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setLastUpdated('200110050000Z')
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setDescription('The MIB module for configuration of bulk distribution (de-multiplexing of traffic from higher-bandwidth to lower-bandwidth interfaces). Terminology : bulk-distribution : The bulk distribution is the feature by which a line/interface on one module can replace the line for the other. bulk-distribution module : The module which links its interfaces to the target module. target module : A module that gets incoming traffic from a bulk distribution module rather than from a back card. The Module which supports bulk distribution, converts traffic from its lines (may be T3, OC-N) to lines on the target module (may be T3, T1 etc). The bulk distribution is achieved by having a point-to-point connection (bulk-distribution bus) between the bulk-distribution module and the target module. The benefit of bulk distribution is that the target module need not have the back cards. The lines/interfaces from bulk-distribution module will be used as lines for the target module. An example is given here on linking interfaces. |------------------------------------------------| | | | |------------------------------| | | | | | | | | | |-------------| | | Ta|rget Module | | | | | ------- ------- ------- --------------- | | | | | | | | | | | | | | | | | T1 | | T1 | |T1 | | Bulk | |card | |card | |card | | Distribution | | | | | | | | | | | | | | | | Module | | | | | | | | | | | | | | | | (T3 card) | | | | | | | | | ------- ------- ------- --------------- ')
cilConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 1))
cilConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1))
cilConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1), )
if mibBuilder.loadTexts: cilConfTable.setStatus('current')
if mibBuilder.loadTexts: cilConfTable.setDescription('The interface link configuration table.')
cilConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-IF-LINK-CONFIG-MIB", "cilSourceInterface"))
if mibBuilder.loadTexts: cilConfEntry.setStatus('current')
if mibBuilder.loadTexts: cilConfEntry.setDescription('An entry in the cilConfTable. This entry is used for linking an interface identified by cilSourceInterface to an interface identified by cilTaregetModuleInterface. The entries are created and deleted using the cilRowStatus object. An interface on the bulk-distribution module cannot be linked to multiple interfaces in the target module.')
cilSourceInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cilSourceInterface.setStatus('current')
if mibBuilder.loadTexts: cilSourceInterface.setDescription('An interface of the bulk-distribution module (Source) which will be linked with the interface of the target module. It represents an entry in the ifTable.')
cilTargetModuleInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 2), CiscoLocationSpecifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilTargetModuleInterface.setStatus('current')
if mibBuilder.loadTexts: cilTargetModuleInterface.setDescription('Location of the managed entity on the target module. Following is the supported format for this object and all the values must be present. shelf=<value>, slot=<value>, subSlot=<value> port =<value>. The zero length value for this object is not supported.')
cilRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilRowStatus.setStatus('current')
if mibBuilder.loadTexts: cilRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in the table. The cilTargetModuleFramingType need not be specified to create a row. If cilTargetModuleFramingType is not specified, a default value will be assumed as described in the description of cilTargetModuleFramingType.')
cilTargetModuleFramingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("dsx1D4", 2), ("dsx1ESF", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilTargetModuleFramingType.setStatus('current')
if mibBuilder.loadTexts: cilTargetModuleFramingType.setDescription('This object identifies the framing type of the target interface. notApplicable(1) can not be set. dsx1ESF Extended SuperFrame DS1 (T1.107) dsx1D4 AT&T D4 format DS1 (T1.107) Default value is dsx1ESF(3) if cilTargetModuleInterface is a T1 interface and sonet/sdh byte-synchronous mapping is used on the cilSourceInterface. Otherwise, the default value is notApplicable(1). ')
cilConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3))
cilConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1))
cilConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2))
cilConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 1)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilConfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfigMIBCompliance = cilConfigMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cilConfigMIBCompliance.setDescription('The Compliance statement for interface link configuration group. This has been replaced by the cilConfigMIBComplianceRev1 statement.')
cilConfigMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 2)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilConfMIBGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfigMIBComplianceRev1 = cilConfigMIBComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: cilConfigMIBComplianceRev1.setDescription('The Compliance statement for interface link configuration group. This statement replaces cilConfigMIBCompliance statement.')
cilConfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 1)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"), ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfMIBGroup = cilConfMIBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cilConfMIBGroup.setDescription('These are objects related to interface link configuration group. This group has been replaced by cilConfMIBGroupRev1.')
cilConfMIBGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 2)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"), ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"), ("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleFramingType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfMIBGroupRev1 = cilConfMIBGroupRev1.setStatus('current')
if mibBuilder.loadTexts: cilConfMIBGroupRev1.setDescription('These are objects related to interface link configuration group. This group replaces the cilConfMIBGroup.')
mibBuilder.exportSymbols("CISCO-IF-LINK-CONFIG-MIB", cilConfMIBGroupRev1=cilConfMIBGroupRev1, cilSourceInterface=cilSourceInterface, cilConfMIBGroup=cilConfMIBGroup, cilTargetModuleInterface=cilTargetModuleInterface, cilConfigMIBObjects=cilConfigMIBObjects, cilConfTable=cilConfTable, cilConfigMIBConformance=cilConfigMIBConformance, cilConfigMIBGroups=cilConfigMIBGroups, cilConfigMIBComplianceRev1=cilConfigMIBComplianceRev1, cilConfigMIBCompliances=cilConfigMIBCompliances, cilConfEntry=cilConfEntry, PYSNMP_MODULE_ID=ciscoIfLinkConfigMIB, cilRowStatus=cilRowStatus, cilTargetModuleFramingType=cilTargetModuleFramingType, cilConfig=cilConfig, ciscoIfLinkConfigMIB=ciscoIfLinkConfigMIB, cilConfigMIBCompliance=cilConfigMIBCompliance)
