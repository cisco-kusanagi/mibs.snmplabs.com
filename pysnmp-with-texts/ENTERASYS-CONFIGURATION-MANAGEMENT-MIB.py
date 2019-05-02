#
# PySNMP MIB module ENTERASYS-CONFIGURATION-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-CONFIGURATION-MANAGEMENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, Counter32, Unsigned32, NotificationType, ObjectIdentity, Counter64, IpAddress, Gauge32, iso, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter32", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter64", "IpAddress", "Gauge32", "iso", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
RowStatus, DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "DateAndTime")
etsysConfigurationManagementMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16))
etsysConfigurationManagementMIB.setRevisions(('2008-12-05 14:13', '2002-10-03 20:21', '2002-09-30 17:02', '2001-12-03 19:49',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysConfigurationManagementMIB.setRevisionsDescriptions(('Added Secure Copy (SCP) as a supported URL type.', 'Updated the Security Considerations section.', 'Added a bootPromDownload bit to the ConfigMgmtOperations textual convention.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysConfigurationManagementMIB.setLastUpdated('200812051413Z')
if mibBuilder.loadTexts: etsysConfigurationManagementMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysConfigurationManagementMIB.setContactInfo('Postal: Enterasys Networks, Inc. 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysConfigurationManagementMIB.setDescription("This MIB module defines a portion of the SNMP MIB under Enterasys Networks' enterprise OID pertaining to configuration management.")
etsysConfigMgmtStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1))
etsysConfigMgmtChange = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2))
etsysConfigMgmtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3))
class ConfigMgmtOperations(TextualConvention, Bits):
    description = 'Operations that can be used to effect the configuration of the managed entity. ------------------------------------------------------- -- Any or all of these operations MAY be supported on -- all devices. ------------------------------------------------------- resetHardware - Initiate a hardware reset. If this operation is requested in conjunction with other operations than this operation should be performed only after all of the other requested operations have completed successfully. resetSoftware - Initiate a software reset. If this operation is requested in conjunction with other operations than this operation should be performed only after all of the other requested operations have completed successfully. imageDownload - The managed entity will initiate an image download using the least disruptive method available to it given the specified protocol. The downloaded image WILL be stored in persistent storage. This operation MAY initiate a reset. bootPromDownload - The managed entity will initiate a boot PROM download using the least disruptive method available to it given the specified protocol. The downloaded boot PROM WILL be stored in persistent storage. This operation MAY initiate a reset. imageDownloadNonPersistent - The managed entity will initiate an image download using the least disruptive method available to it given the specified protocol. This operation WILL cause the managed entity to reset. The managed entity will not execute the new image on subsequent resets. configurationReset - Reset the configuration to the factory default state. This operation MAY initiate a reset. configurationUpload - The managed entity will transfer the currently active configuration to the specified destination. The destination may be a local file on entities that support a user file system. configurationDownload - The managed entity will initiate a configuration file download using the least disruptive method available to it given the specified protocol. The downloaded configuration WILL be stored in persistent storage. This operation MAY cause the managed entity to reset. validationMD5sum, - The system will calculate the MD5 message digest, as specified in RFC1321, for the file specified in etsysConfigMgmtChangeURL and compare that with the value of the etsysConfigMgmtChangeValidationString object. If this operation is requested in conjunction with other operations then this operation MUST be initiated as soon as practical and all operations MUST be terminated/aborted as soon as practical if the calculated value does not match the specified value. If the etsysConfigMgmtChangeValidationString is empty the calculate the MD5 message digest will be returned in that object. ------------------------------------------------------- -- Any or all of these operations MAY be supported on -- devices that have user file systems. ------------------------------------------------------- imageSetSelected - The file specified in etsysConfigMgmtChangeURL is selected as the boot image. Although a reset MAY be required to execute the selected boot image this operation WILL NOT initiate a reset. This operation will fail if the specified file is not a valid boot image. imageGetSelected - The file selected as the boot image is returned in etsysConfigMgmtChangeURL. This operation MUST NOT be used in conjunction with any other operations. configurationActivate - The configuration file specified in the etsysConfigMgmtChangeURL is applied to the factory default configuration and the result becomes the active configuration. If the entity does not support the configurationPersist operation the result also becomes the start-up configuration. This operation MAY initiate a reset operation. configurationAppend - The configuration file specified in the etsysConfigMgmtChangeURL is applied to the active configuration and the result becomes the active configuration. If the entity does not support the configurationPersist operation the result also becomes the start-up configuration. This operation SHOULD NOT initiate a reset operation. configurationPersist - The active configuration will be save to persistent storage and become the start-up configuration. This operation WILL NOT initiate a reset operation. configurationParse - The configuration file specified in the etsysConfigMgmtChangeURL is parsed for errors. This operation WILL NOT effect active configuration. This operation WILL NOT initiate a reset operation.'
    status = 'current'
    namedValues = NamedValues(("resetHardware", 0), ("resetSoftware", 1), ("imageDownload", 2), ("imageDownloadNonPersistent", 3), ("configurationReset", 4), ("configurationUpload", 5), ("configurationDownload", 6), ("imageSetSelected", 7), ("imageGetSelected", 8), ("configurationActivate", 9), ("configurationAppend", 10), ("configurationPersist", 11), ("configurationParse", 12), ("validationMD5sum", 13), ("bootPromDownload", 14))

etsysConfigMgmtCurrentImageURL = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 1), DisplayString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtCurrentImageURL.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtCurrentImageURL.setDescription('The URL of the last image to be successfully loaded into memory. Return an empty string if this feature is not supported or the information is unavailable.')
etsysConfigMgmtCurrentConfigURL = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 2), DisplayString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtCurrentConfigURL.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtCurrentConfigURL.setDescription('The URL of the last configuration file to be successfully loaded into memory. Return an empty string if this feature is not supported or the information is unavailable.')
etsysConfigMgmtPersistentStorageStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 3), DisplayString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtPersistentStorageStatus.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtPersistentStorageStatus.setDescription("A descriptive status of any current failures of any of the persistent storage facilities on this entity. When this information is unavailable return a null string. 'operational' should be returned if there are no problems. Transitional information MAY be reported as well.")
etsysConfigMgmtPersistentStorageCkSum = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 4), DisplayString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtPersistentStorageCkSum.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtPersistentStorageCkSum.setDescription('The MD5 message digest, as specified in RFC1321, for the persistent configuration information. This object MAY be used by management applications to detect changes to the configuration of the managed entity. If it is not possible to compute this value return an empty string.')
etsysConfigMgmtChangeLimit = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeLimit.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeLimit.setDescription('The maximum number of configuration change requests this entity can hold in the etsysConfigMgmtChangeTable. A value of 0 indicates no configured limit.')
etsysConfigMgmtChangeCurrent = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeCurrent.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeCurrent.setDescription('The number of configuration change requests currently in the etsysConfigMgmtChangeTable.')
etsysConfigMgmtChangeCompleted = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeCompleted.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeCompleted.setDescription('The number of configuration change requests that have completed successfully or otherwise. This object should be stored in persistent memory.')
etsysConfigMgmtChangeSupportedURLs = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 4), Bits().clone(namedValues=NamedValues(("etsysConfigMgmtFtp", 0), ("etsysConfigMgmtRcp", 1), ("etsysConfigMgmtHttp", 2), ("etsysConfigMgmtTftp", 3), ("etsysConfigMgmtFile", 4), ("etsysConfigMgmtBootP", 5), ("etsysConfigMgmtScp", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeSupportedURLs.setReference('RFC 1738 - Uniform Resource Locators (URL), RFC 2396 - Uniform Resource Identifiers (URI): Generic Syntax')
if mibBuilder.loadTexts: etsysConfigMgmtChangeSupportedURLs.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeSupportedURLs.setDescription('The URLs that this entity supports for transferring files. These define the transfer protocols and remote file names. etsysConfigMgmtFtp - As per rfc1738 ftp://<user>:<password>@<host>:<port>/<url-path> url-path: <cwd1>/<cwd2>/.../<cwdN>/<name>;type=<typecode> user defaults to anonymous, password to snmp@<domain-name>, port to 21, and type to ASCII. binary and image are both valid types which have the same meaning. domain-name would be the IP address or domain name of the managed entity. etsysConfigMgmtRcp - rcp://<user>@<host>:<port>/<cwd1>/<cwd2>/.../<cwdN>/<name> port defaults to 514. etsysConfigMgmtHttp - As per rfc1738 http://<host>:<port>/<path>?<searchpart> port defaults to 80. etsysConfigMgmtTftp - tftp://<host>:<port>/<cwd1>/<cwd2>/.../<cwdN>/<name> port defaults to 69. etsysConfigMgmtFile - As per rfc1738 file://<host>/<path> host can only be specified as localhost or the empty string. This will only be used to specify a file on the managed entity. This indicates that the managed entity supports some form of a user file system. etsysConfigMgmtBootP - bootp://<host> host specifies the default gateway, or bootp server that the bootp request should be directed to. etsysConfigMgmtScp - scp://<user>:<password>@<host>:<port>/<cwd1>/<cwd2>/.../<cwdN>/<name> host as defined in RFC1738. port defaults to 22.')
etsysConfigMgmtChangeSupportedOperations = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 5), ConfigMgmtOperations()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeSupportedOperations.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeSupportedOperations.setDescription('Configuration change operations that are supported on this managed entity. A managed entity should provide support only for the options that make sense given the capabilities of the entity and the desired level of manageability.')
etsysConfigMgmtChangeNextAvailableIndex = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeNextAvailableIndex.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeNextAvailableIndex.setDescription('This object indicates the numerically lowest available index within this entity, which may be used for the value of etsysConfigMgmtChangeIndex in the creation of a new entry in the etsysConfigMgmtChangeTable. An index is considered available if the index value falls within the range of 1 to etsysConfigMgmtChangeLimit and is not being used to index an existing entry in the etsysConfigMgmtChangeTable contained within this entity. A value of zero indicates that all of the entries in the etsysConfigMgmtChangeTable are currently in use. This value should only be considered a guideline for management creation of etsysConfigMgmtChangeTable entries, there is no requirement on management to create entries based upon this index value.')
etsysConfigMgmtChangeTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7), )
if mibBuilder.loadTexts: etsysConfigMgmtChangeTable.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeTable.setDescription('A table that describes a single configuration change request.')
etsysConfigMgmtChangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1), ).setIndexNames((0, "ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeIndex"))
if mibBuilder.loadTexts: etsysConfigMgmtChangeEntry.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeEntry.setDescription('An entry describing the configuration change request.')
etsysConfigMgmtChangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: etsysConfigMgmtChangeIndex.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeIndex.setDescription('The index for this configuration change request.')
etsysConfigMgmtChangeURL = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 2), DisplayString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysConfigMgmtChangeURL.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeURL.setDescription('The URL of the image, configuration file, or server to use for the requested operation. Any password information MUST NOT be returned on a read. Any errors with the type or format of this object SHOULD be reported in the etsysConfigMgmtChangeErrorDescription object when the row is activated.')
etsysConfigMgmtChangeOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 3), ConfigMgmtOperations()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysConfigMgmtChangeOperation.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeOperation.setDescription('The operation or operations requested. The specification of any unsupported operations SHOULD cause the entire operation to fail immediately and an appropriate error description to be generated.')
etsysConfigMgmtChangeOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("inactive", 1), ("pending", 2), ("running", 3), ("success", 4), ("failure", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeOperStatus.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeOperStatus.setDescription('The operational state of the configuration request. inactive - Indicates that the RowStatus of this conceptual row is not in the `active` state. pending - Indicates that the configuration change described by this row is ready to run and waiting in a queue. running - Indicates that the configuration change described by this row is running. success - Indicates that the configuration change described by this row has successfully run to completion. failure - Indicates that the configuration change described by this row has failed to run to completion.')
etsysConfigMgmtChangeDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysConfigMgmtChangeDelayTime.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeDelayTime.setDescription('The number of seconds that should elapse between the time that the RowStatus of this conceptual row is set to active and the request is queued for execution. On a read this object should return the time remaining before the request is queued.')
etsysConfigMgmtChangeEnqueuedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 6), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeEnqueuedTime.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeEnqueuedTime.setDescription("The date and time, in device local time, when this change request was last enqueued for execution. The value '0000000000000000'H is returned if this table entry has not yet been queued.")
etsysConfigMgmtChangeCompletionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 7), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeCompletionTime.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeCompletionTime.setDescription("The date and time, in device local time, when this change request was last completed. It should be reset to the default value when the RowStatus of this conceptual row is set to active. The value '0000000000000000'H is returned if this table entry has not yet run to completion.")
etsysConfigMgmtChangeBytesTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeBytesTransferred.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeBytesTransferred.setDescription('The number of bytes currently transferred. A value of -1 indicates that this feature is not supported for the protocol currently selected. This value is reset to its initial state when the etsysConfigMgmtRowStatus object is set to the active state.')
etsysConfigMgmtChangeValidationString = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 9), DisplayString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysConfigMgmtChangeValidationString.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeValidationString.setDescription('A checksum, fingerprint, message-digest, or some other means to validate the integrity of the file.')
etsysConfigMgmtChangeErrorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 10), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeErrorDescription.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeErrorDescription.setDescription('This object contains a descriptive error message if the requested transfer failed. Implementations must reset the error message to a zero-length string when the etsysConfigMgmtChangeRowStatus leaf is set to the active state.')
etsysConfigMgmtChangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysConfigMgmtChangeRowStatus.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeRowStatus.setDescription("A control that will allow one entry to be added, activated, deactivated, and removed from this table. When the value of this object is 'active' none of the other objects in this conceptual row can be modified. Setting this object to the 'active' state from the 'notInService' state will cause the requested configuration operation to be initiated. Once the requested configuration operation has completed, successfully or otherwise, this leaf will be set to the 'notInService' state by the managed entity. Setting this object to any other valid state from the 'active' state SHOULD cause the managed entity to cancel the requested operation at its earliest most rational opportunity. Setting this object to the 'active' state from the 'active' state SHOULD NOT have any affect. Conceptual rows that have been in the 'notInService' state for more than a device specific time period MAY be destroyed by the managed entity.")
etsysConfigMgmtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 1))
etsysConfigMgmtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 2))
etsysConfigMgmtStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 1, 1)).setObjects(("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtCurrentImageURL"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtCurrentConfigURL"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtPersistentStorageStatus"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtPersistentStorageCkSum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysConfigMgmtStatusGroup = etsysConfigMgmtStatusGroup.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtStatusGroup.setDescription("Objects that provide some status information about the entity's current configuration.")
etsysConfigMgmtChangeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 1, 2)).setObjects(("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeLimit"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeCurrent"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeCompleted"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeSupportedURLs"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeSupportedOperations"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeNextAvailableIndex"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeURL"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeOperation"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeOperStatus"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeDelayTime"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeEnqueuedTime"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeCompletionTime"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeBytesTransferred"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeValidationString"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeErrorDescription"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysConfigMgmtChangeGroup = etsysConfigMgmtChangeGroup.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtChangeGroup.setDescription("Objects that provide a means to change the entity's configuration.")
etsysConfigMgmtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 2, 1)).setObjects(("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtStatusGroup"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysConfigMgmtCompliance = etsysConfigMgmtCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysConfigMgmtCompliance.setDescription('The compliance statement for entities which implement the Enterasys Configuration Management MIB. Implementation of this MIB is based on individual product needs.')
mibBuilder.exportSymbols("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", etsysConfigMgmtChangeCurrent=etsysConfigMgmtChangeCurrent, etsysConfigMgmtPersistentStorageStatus=etsysConfigMgmtPersistentStorageStatus, ConfigMgmtOperations=ConfigMgmtOperations, etsysConfigMgmtChangeRowStatus=etsysConfigMgmtChangeRowStatus, etsysConfigMgmtStatusGroup=etsysConfigMgmtStatusGroup, etsysConfigMgmtPersistentStorageCkSum=etsysConfigMgmtPersistentStorageCkSum, etsysConfigMgmtChangeCompletionTime=etsysConfigMgmtChangeCompletionTime, PYSNMP_MODULE_ID=etsysConfigurationManagementMIB, etsysConfigMgmtCompliances=etsysConfigMgmtCompliances, etsysConfigMgmtChangeErrorDescription=etsysConfigMgmtChangeErrorDescription, etsysConfigMgmtCompliance=etsysConfigMgmtCompliance, etsysConfigMgmtStatus=etsysConfigMgmtStatus, etsysConfigMgmtGroups=etsysConfigMgmtGroups, etsysConfigMgmtCurrentImageURL=etsysConfigMgmtCurrentImageURL, etsysConfigMgmtChangeSupportedOperations=etsysConfigMgmtChangeSupportedOperations, etsysConfigMgmtChangeCompleted=etsysConfigMgmtChangeCompleted, etsysConfigMgmtChangeLimit=etsysConfigMgmtChangeLimit, etsysConfigMgmtChangeBytesTransferred=etsysConfigMgmtChangeBytesTransferred, etsysConfigMgmtChangeIndex=etsysConfigMgmtChangeIndex, etsysConfigMgmtChangeGroup=etsysConfigMgmtChangeGroup, etsysConfigMgmtChangeURL=etsysConfigMgmtChangeURL, etsysConfigMgmtCurrentConfigURL=etsysConfigMgmtCurrentConfigURL, etsysConfigMgmtConformance=etsysConfigMgmtConformance, etsysConfigMgmtChange=etsysConfigMgmtChange, etsysConfigMgmtChangeSupportedURLs=etsysConfigMgmtChangeSupportedURLs, etsysConfigMgmtChangeTable=etsysConfigMgmtChangeTable, etsysConfigMgmtChangeNextAvailableIndex=etsysConfigMgmtChangeNextAvailableIndex, etsysConfigMgmtChangeEntry=etsysConfigMgmtChangeEntry, etsysConfigMgmtChangeDelayTime=etsysConfigMgmtChangeDelayTime, etsysConfigMgmtChangeOperation=etsysConfigMgmtChangeOperation, etsysConfigurationManagementMIB=etsysConfigurationManagementMIB, etsysConfigMgmtChangeValidationString=etsysConfigMgmtChangeValidationString, etsysConfigMgmtChangeEnqueuedTime=etsysConfigMgmtChangeEnqueuedTime, etsysConfigMgmtChangeOperStatus=etsysConfigMgmtChangeOperStatus)
