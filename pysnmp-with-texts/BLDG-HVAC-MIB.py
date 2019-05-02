#
# PySNMP MIB module BLDG-HVAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLDG-HVAC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:39:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, NotificationType, ObjectIdentity, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, MibIdentifier, experimental, Unsigned32, ModuleIdentity, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "ObjectIdentity", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "MibIdentifier", "experimental", "Unsigned32", "ModuleIdentity", "Bits", "Gauge32")
StorageType, RowStatus, TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "TextualConvention", "TimeStamp", "DisplayString")
bldgHVACMIB = ModuleIdentity((1, 3, 6, 1, 3, 122))
bldgHVACMIB.setRevisions(('2003-03-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bldgHVACMIB.setRevisionsDescriptions(('Initial version of BLDG-HVAC-MIB as published in RFC 3512.',))
if mibBuilder.loadTexts: bldgHVACMIB.setLastUpdated('200303270000Z')
if mibBuilder.loadTexts: bldgHVACMIB.setOrganization('SNMPCONF working group E-mail: snmpconf@snmp.com')
if mibBuilder.loadTexts: bldgHVACMIB.setContactInfo('Jon Saperia Postal: JDS Consulting 174 Chapman Street Watertown, MA 02472 U.S.A. Phone: +1 617 744 1079 E-mail: saperia@jdscons.com Wayne Tackabury Postal: Gold Wire Technology 411 Waverley Oaks Rd. Waltham, MA 02452 U.S.A. Phone: +1 781 398 8800 E-mail: wayne@goldwiretech.com Michael MacFaden Postal: Riverstone Networks 5200 Great America Pkwy. Santa Clara, CA 95054 U.S.A. Phone: +1 408 878 6500 E-mail: mrm@riverstonenet.com David Partain Postal: Ericsson AB P.O. Box 1248 SE-581 12 Linkoping Sweden E-mail: David.Partain@ericsson.com')
if mibBuilder.loadTexts: bldgHVACMIB.setDescription('This example MIB module defines a set of management objects for heating ventilation and air conditioning systems. It also includes objects that can be used to create policies that are applied to rooms. This eliminates the need to send per-instance configuration commands to the system. Copyright (C) The Internet Society (2003). This version of this MIB module is part of RFC 3512; see the RFC itself for full legal notices.')
bldgHVACObjects = MibIdentifier((1, 3, 6, 1, 3, 122, 1))
bldgConformance = MibIdentifier((1, 3, 6, 1, 3, 122, 2))
class BldgHvacOperation(TextualConvention, Integer32):
    description = 'Operations supported by a heating and cooling system. A reference to underlying general systems would go here.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("heat", 1), ("cool", 2))

bldgHVACTable = MibTable((1, 3, 6, 1, 3, 122, 1, 1), )
if mibBuilder.loadTexts: bldgHVACTable.setStatus('current')
if mibBuilder.loadTexts: bldgHVACTable.setDescription('This table is the representation and data control for building HVAC by each individual office. The table has rows for, and is indexed by a specific floor and office number. Each such row includes HVAC statistical and current status information for the associated office. The row also contains a bldgHVACCfgTemplate columnar object that relates the bldgHVACTable row to a row in the bldgHVACCfgTemplateTable. If this value is nonzero, then the instance in the row that has a value for how the HVAC has been configured in the associated template (bldgHVACCfgTeplateTable row). Hence, the bldgHVACCfgTeplateTable row contains the specific configuration values for the offices as described in this table.')
bldgHVACEntry = MibTableRow((1, 3, 6, 1, 3, 122, 1, 1, 1), ).setIndexNames((0, "BLDG-HVAC-MIB", "bldgHVACFloor"), (0, "BLDG-HVAC-MIB", "bldgHVACOffice"))
if mibBuilder.loadTexts: bldgHVACEntry.setStatus('current')
if mibBuilder.loadTexts: bldgHVACEntry.setDescription('A row in the bldgHVACTable. Each row represents a particular office in the building, qualified by its floor and office number. A given row instance can be created or deleted by set operations upon its bldgHVACStatus columnar object instance.')
bldgHVACFloor = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: bldgHVACFloor.setStatus('current')
if mibBuilder.loadTexts: bldgHVACFloor.setDescription('This portion of the index indicates the floor of the building. The ground floor is considered the first floor. For the purposes of this example, floors under the ground floor cannot be controlled using this MIB module.')
bldgHVACOffice = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: bldgHVACOffice.setStatus('current')
if mibBuilder.loadTexts: bldgHVACOffice.setDescription('This second component of the index specifies the office number.')
bldgHVACCfgTemplate = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplate.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplate.setDescription("The index (bldgHVACCfgTemplateIndex instance) of an entry in the 'bldgHVACCfgTemplateTable'. The bldgHVACCfgTable row instance referenced is a pre-made configuration 'template' that represents the configuration described by the bldgHVACCfgTemplateInfoDescr object. Note that not all configurations will be under a defined template. As a result, a row in this bldgHVACTable may point to an entry in the bldgHVACCfgTemplateTable that does not in turn have a reference (bldgHVACCfgTemplateInfo) to an entry in the bldgHVACCfgTemplateInfoTable. The benefit of this approach is that all configuration information is available in one table whether all elements in the system are derived from configured templates or not. Where the instance value for this colunmar object is zero, this row represents data for an office whose HVAC status can be monitored using the read-only columnar object instances of this row, but is not under the configuration control of the agent.")
bldgHVACFanSpeed = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 1, 1, 4), Gauge32()).setUnits('revolutions per minute').setMaxAccess("readonly")
if mibBuilder.loadTexts: bldgHVACFanSpeed.setStatus('current')
if mibBuilder.loadTexts: bldgHVACFanSpeed.setDescription('Shows the revolutions per minute of the fan. Fan speed will vary based on the difference between bldgHVACCfgTemplateDesiredTemp and bldgHVACCurrentTemp. The speed is measured in revolutions of the fan blade per minute.')
bldgHVACCurrentTemp = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 1, 1, 5), Gauge32()).setUnits('degrees in celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: bldgHVACCurrentTemp.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCurrentTemp.setDescription('The current measured temperature in the office. Should the current temperature be measured at a value of less than zero degrees celsius, a read of the instance for this object will return a value of zero.')
bldgHVACCoolOrHeatMins = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 1, 1, 6), Counter32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: bldgHVACCoolOrHeatMins.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCoolOrHeatMins.setDescription('The total number of heating or cooling minutes that have been consumed since the row was activated. Notice that whether the minutes represent heating or cooling is a function of the configuration of this row. If the system is re-initialized from a cooling to heating function or vice versa, then the counter would start over again. This effect is similar to a reconfiguration of some network interface cards. When parameters that impact configuration are changed, the subsystem must be re-initialized. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of bldgHVACDiscontinuityTime.')
bldgHVACDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bldgHVACDiscontinuityTime.setStatus('current')
if mibBuilder.loadTexts: bldgHVACDiscontinuityTime.setDescription('The value of sysUpTime on the most recent occasion at which any heating or cooling operation for the office designated by this row instance experienced a discontinuity. If no such discontinuities have occurred since the last re- initialization of the this row, then this object contains a zero value.')
bldgHVACOwner = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACOwner.setStatus('current')
if mibBuilder.loadTexts: bldgHVACOwner.setDescription("The identity of the operator/system that last modified this entry. When a new entry is created, a valid SnmpAdminString must be supplied. If, on the other hand, this entry is populated by the agent 'discovering' unconfigured rooms, the empty string is a valid value for this object.")
bldgHVACStorageType = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 1, 1, 9), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACStorageType.setStatus('current')
if mibBuilder.loadTexts: bldgHVACStorageType.setDescription("The persistence of this row of the table in system storage, as it pertains to permanence across system resets. A columnar instance of this object with value 'permanent' need not allow write-access to any of the columnar object instances in the containing row.")
bldgHVACStatus = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACStatus.setStatus('current')
if mibBuilder.loadTexts: bldgHVACStatus.setDescription('Controls and reflects the creation and activation status of a row in this table. No attempt to modify a row columnar object instance value in the bldgHVACTable should be issued while the value of bldgHVACStatus is active(1). Should an agent receive a SET PDU attempting such a modification in this state, an inconsistentValue error should be returned as a result of the SET attempt.')
bldgHVACCfgTemplateInfoTable = MibTable((1, 3, 6, 1, 3, 122, 1, 2), )
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoTable.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoTable.setDescription('This table provides unique string identification for HVAC templates in a network. If it were necessary to configure rooms to deliver a particular quality of climate control with regard to cooling or heating, the index string of a row in this table could be the template name. The bldgHVACCfgCfgTemplateInfoDescription contains a brief description of the template service objective such as: provides summer cooling settings for executive offices. The bldgHVACCfgTemplateInfo in the bldgHVACCfgTemplateTable will contain the pointer to the relevant row in this table if it is intended that items that point to a row in the bldgHVACCfgTemplateInfoTable be identifiable as being under template control though this mechanism.')
bldgHVACCfgTemplateInfoEntry = MibTableRow((1, 3, 6, 1, 3, 122, 1, 2, 1), ).setIndexNames((0, "BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoIndex"))
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoEntry.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoEntry.setDescription('Each row represents a particular template and description. A given row instance can be created or deleted by set operations upon its bldgHVACCfgTemplateInfoStatus columnar object instance.')
bldgHVACCfgTemplateInfoIndex = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoIndex.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoIndex.setDescription('The unique index to a row in this table.')
bldgHVACCfgTemplateInfoID = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoID.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoID.setDescription("Textual identifier for this table row, and, consequently the template. This should be a unique name within an administrative domain for a particular template so that all systems in a network that are under the same template can have the same 'handle' (e.g., 'Executive Offices', 'Lobby Areas').")
bldgHVACCfgTemplateInfoDescr = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoDescr.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoDescr.setDescription('A general description of the template. One example might be - Controls the cooling for offices on higher floors during the summer.')
bldgHVACCfgTemplateInfoOwner = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 2, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoOwner.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoOwner.setDescription('The identity of the operator/system that last modified this entry.')
bldgHVACCfgTemplateInfoStatus = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoStatus.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoStatus.setDescription('The activation status of this row. No attempt to modify a row columnar object instance value in the bldgHVACCfgTemplateInfo Table should be issued while the value of bldgHVACCfgTemplateInfoStatus is active(1). Should an agent receive a SET PDU attempting such a modification in this state, an inconsistentValue error should be returned as a result of the SET attempt.')
bldgHVACCfgTemplateInfoStorType = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 2, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoStorType.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfoStorType.setDescription("The persistence of this row of the table in system storage, as it pertains to permanence across system resets. A columnar instance of this object with value 'permanent' need not allow write-access to any of the columnar object instances in the containing row.")
bldgHVACCfgTemplateTable = MibTable((1, 3, 6, 1, 3, 122, 1, 3), )
if mibBuilder.loadTexts: bldgHVACCfgTemplateTable.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateTable.setDescription("This table contains the templates, which can be used to set defaults that will be applied to specific offices. The application of those values is accomplished by having a row instance of the bldgHVACTable reference a row of this table (by the value of the former's bldgHVACCfgTemplate columnar instance). Identifying information concerning a row instance of this table can be found in the columnar data of the row instance of the bldgHVACCfgTemplateInfoTable entry referenced by the bldgHVACCfgTemplateInfo columnar object of this table.")
bldgHVACCfgTemplateEntry = MibTableRow((1, 3, 6, 1, 3, 122, 1, 3, 1), ).setIndexNames((0, "BLDG-HVAC-MIB", "bldgHVACCfgTemplateIndex"))
if mibBuilder.loadTexts: bldgHVACCfgTemplateEntry.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateEntry.setDescription('Each row represents a single set of template parameters that can be applied to selected instances - in this case offices. These policies will be turned on and off by the policy module through its scheduling facilities. A given row instance can be created or deleted by set operations upon its bldgHVACCfgTemplateStatus columnar object instance.')
bldgHVACCfgTemplateIndex = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: bldgHVACCfgTemplateIndex.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateIndex.setDescription('A unique value for each defined template in this table. This value can be referenced as a row index by any MIB module that needs access to this information. The bldgHVACCfgTemplate will point to entries in this table.')
bldgHVACCfgTemplateDesiredTemp = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 3, 1, 2), Gauge32()).setUnits('degrees in celsius').setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplateDesiredTemp.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateDesiredTemp.setDescription('This is the desired temperature setting. It might be changed at different times of the day or based on seasonal conditions. It is permitted to change this value by first moving the row to an inactive state, making the change and then reactivating the row.')
bldgHVACCfgTemplateCoolOrHeat = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 3, 1, 3), BldgHvacOperation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplateCoolOrHeat.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateCoolOrHeat.setDescription('This controls the heating and cooling mechanism and is set-able by building maintenance. It is permitted to change this value by first moving the row to an inactive state, making the change and then reactivating the row.')
bldgHVACCfgTemplateInfo = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfo.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateInfo.setDescription('This object points to a row in the bldgHVACCfgTemplateInfoTable. This controls the heating and cooling mechanism and is set-able by building maintenance. It is permissible to change this value by first moving the row to an inactive state, making the change and then reactivating the row. A value of zero means that this entry is not associated with a named template found in the bldgHVACCfgTemplateInfoTable.')
bldgHVACCfgTemplateOwner = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 3, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplateOwner.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateOwner.setDescription('The identity of the administrative entity that created this row of the table.')
bldgHVACCfgTemplateStorage = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 3, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplateStorage.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateStorage.setDescription("The persistence of this row of the table across system resets. A columnar instance of this object with value 'permanent' need not allow write-access to any of the columnar object instances in the containing row.")
bldgHVACCfgTemplateStatus = MibTableColumn((1, 3, 6, 1, 3, 122, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bldgHVACCfgTemplateStatus.setStatus('current')
if mibBuilder.loadTexts: bldgHVACCfgTemplateStatus.setDescription('The activation status of this row of the table. No attempt to modify a row columnar object instance value in the bldgHVACCfgTemplateTable should be issued while the value of bldgHVACCfgTemplateStatus is active(1). Should an agent receive a SET PDU attempting such a modification in this state, an inconsistentValue error should be returned as a result of the SET attempt.')
bldgCompliances = MibIdentifier((1, 3, 6, 1, 3, 122, 2, 1))
bldgGroups = MibIdentifier((1, 3, 6, 1, 3, 122, 2, 2))
bldgCompliance = ModuleCompliance((1, 3, 6, 1, 3, 122, 2, 1, 1)).setObjects(("BLDG-HVAC-MIB", "bldgHVACObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bldgCompliance = bldgCompliance.setStatus('current')
if mibBuilder.loadTexts: bldgCompliance.setDescription('The requirements for conformance to the BLDG-HVAC-MIB. The bldgHVACObjects group must be implemented to conform to the BLDG-HVAC-MIB.')
bldgHVACObjectsGroup = ObjectGroup((1, 3, 6, 1, 3, 122, 2, 2, 1)).setObjects(("BLDG-HVAC-MIB", "bldgHVACCfgTemplate"), ("BLDG-HVAC-MIB", "bldgHVACFanSpeed"), ("BLDG-HVAC-MIB", "bldgHVACCurrentTemp"), ("BLDG-HVAC-MIB", "bldgHVACCoolOrHeatMins"), ("BLDG-HVAC-MIB", "bldgHVACDiscontinuityTime"), ("BLDG-HVAC-MIB", "bldgHVACOwner"), ("BLDG-HVAC-MIB", "bldgHVACStatus"), ("BLDG-HVAC-MIB", "bldgHVACStorageType"), ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoID"), ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoDescr"), ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoOwner"), ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoStatus"), ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoStorType"), ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateDesiredTemp"), ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateCoolOrHeat"), ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfo"), ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateOwner"), ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateStorage"), ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bldgHVACObjectsGroup = bldgHVACObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: bldgHVACObjectsGroup.setDescription('The bldgHVACObjects Group.')
mibBuilder.exportSymbols("BLDG-HVAC-MIB", bldgHVACCfgTemplateInfoEntry=bldgHVACCfgTemplateInfoEntry, bldgHVACCoolOrHeatMins=bldgHVACCoolOrHeatMins, bldgHVACCfgTemplateIndex=bldgHVACCfgTemplateIndex, bldgCompliances=bldgCompliances, bldgHVACMIB=bldgHVACMIB, bldgHVACStatus=bldgHVACStatus, bldgCompliance=bldgCompliance, bldgHVACCfgTemplateStorage=bldgHVACCfgTemplateStorage, bldgHVACCfgTemplateTable=bldgHVACCfgTemplateTable, bldgHVACCfgTemplateInfoStorType=bldgHVACCfgTemplateInfoStorType, bldgHVACCfgTemplate=bldgHVACCfgTemplate, bldgHVACCfgTemplateInfoOwner=bldgHVACCfgTemplateInfoOwner, bldgHVACStorageType=bldgHVACStorageType, PYSNMP_MODULE_ID=bldgHVACMIB, bldgHVACCfgTemplateInfoID=bldgHVACCfgTemplateInfoID, bldgHVACCfgTemplateOwner=bldgHVACCfgTemplateOwner, bldgHVACFloor=bldgHVACFloor, bldgHVACCfgTemplateInfoIndex=bldgHVACCfgTemplateInfoIndex, bldgHVACObjects=bldgHVACObjects, bldgHVACTable=bldgHVACTable, bldgConformance=bldgConformance, bldgHVACCfgTemplateDesiredTemp=bldgHVACCfgTemplateDesiredTemp, bldgHVACObjectsGroup=bldgHVACObjectsGroup, bldgHVACFanSpeed=bldgHVACFanSpeed, bldgHVACEntry=bldgHVACEntry, bldgHVACCfgTemplateCoolOrHeat=bldgHVACCfgTemplateCoolOrHeat, BldgHvacOperation=BldgHvacOperation, bldgGroups=bldgGroups, bldgHVACOwner=bldgHVACOwner, bldgHVACDiscontinuityTime=bldgHVACDiscontinuityTime, bldgHVACCfgTemplateStatus=bldgHVACCfgTemplateStatus, bldgHVACCurrentTemp=bldgHVACCurrentTemp, bldgHVACCfgTemplateInfoStatus=bldgHVACCfgTemplateInfoStatus, bldgHVACCfgTemplateEntry=bldgHVACCfgTemplateEntry, bldgHVACCfgTemplateInfoDescr=bldgHVACCfgTemplateInfoDescr, bldgHVACCfgTemplateInfo=bldgHVACCfgTemplateInfo, bldgHVACCfgTemplateInfoTable=bldgHVACCfgTemplateInfoTable, bldgHVACOffice=bldgHVACOffice)
