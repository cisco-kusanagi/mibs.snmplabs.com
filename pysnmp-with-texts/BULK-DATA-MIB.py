#
# PySNMP MIB module BULK-DATA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BULK-DATA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:42:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, Counter64, Gauge32, Counter32, experimental, Unsigned32, Bits, MibIdentifier, IpAddress, iso, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Counter64", "Gauge32", "Counter32", "experimental", "Unsigned32", "Bits", "MibIdentifier", "IpAddress", "iso", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, RowStatus, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TimeStamp")
bulkDataMIB = ModuleIdentity((1, 3, 6, 1, 3, 999))
if mibBuilder.loadTexts: bulkDataMIB.setLastUpdated('200228021100Z')
if mibBuilder.loadTexts: bulkDataMIB.setOrganization('EOS (Evolution of SNMP)')
if mibBuilder.loadTexts: bulkDataMIB.setContactInfo('Bryan Levin, Allegro Networks Postal: 6399 San Ignacio San Jose, CA 95119-1206 Tel: +1 408 281-5500 E-mail: snmp@allegronetworks.com David Battle, Cisco Systems Postal: Tel: +1 E-mail: dbattle@cisco.com')
if mibBuilder.loadTexts: bulkDataMIB.setDescription('The MIB module for defining Bulk Data objects along with the Bulk Data file format, Upload Fileserver and Data Slice.')
bulkDataAgentCapabilities = MibIdentifier((1, 3, 6, 1, 3, 999, 1))
bulkDataObjects = MibIdentifier((1, 3, 6, 1, 3, 999, 2))
bulkDataTraps = MibIdentifier((1, 3, 6, 1, 3, 999, 3))
acFileEncoding = MibScalar((1, 3, 6, 1, 3, 999, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ascii", 1), ("xml", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acFileEncoding.setStatus('current')
if mibBuilder.loadTexts: acFileEncoding.setDescription("This describes the agent's capability in term of which file encoding styles it supports.")
acFileCompression = MibScalar((1, 3, 6, 1, 3, 999, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noCompression", 1), ("bzip", 2), ("gzip", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acFileCompression.setStatus('current')
if mibBuilder.loadTexts: acFileCompression.setDescription("This describes the agent's capability in term of which file compression styles it supports.")
acXferProtocol = MibScalar((1, 3, 6, 1, 3, 999, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cp", 1), ("ftp", 2), ("scp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acXferProtocol.setStatus('current')
if mibBuilder.loadTexts: acXferProtocol.setDescription("This describes the agent's capability in term of which file transfer protocols it supports.")
sliceTable = MibTable((1, 3, 6, 1, 3, 999, 2, 1), )
if mibBuilder.loadTexts: sliceTable.setStatus('current')
if mibBuilder.loadTexts: sliceTable.setDescription("This table describes a bulk data slice that is a user- defined subset of the current running agent's MIB data. Virtual tables are built by specifying a sequence of columnar Object Identifiers from real mib tables.")
sliceEntry = MibTableRow((1, 3, 6, 1, 3, 999, 2, 1, 1), ).setIndexNames((0, "BULK-DATA-MIB", "sliceIndex"), (0, "BULK-DATA-MIB", "sliceSubId"))
if mibBuilder.loadTexts: sliceEntry.setStatus('current')
if mibBuilder.loadTexts: sliceEntry.setDescription('The data slice entry.')
sliceIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: sliceIndex.setStatus('current')
if mibBuilder.loadTexts: sliceIndex.setDescription('An arbitrary integer to uniquely identify this entry. To create an entry a management application should pick a random number.')
sliceSubId = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: sliceSubId.setStatus('current')
if mibBuilder.loadTexts: sliceSubId.setDescription('A sequential sub-index to identify a component of a slice entry.')
sliceColumnOID = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sliceColumnOID.setStatus('current')
if mibBuilder.loadTexts: sliceColumnOID.setDescription('An Object Identifier, which must refer to a column of a conceptual table. A slice is defined to be a series of columns OIDs that exist in various tables which are accessible via the local agent.')
sliceSnmpContext = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sliceSnmpContext.setStatus('current')
if mibBuilder.loadTexts: sliceSnmpContext.setDescription('In mib groups that are not inherently instancable, an snmp manager context is used to multiply access the separate instances (eg, the bridge mib).')
sliceColumnDisplayHint = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sliceColumnDisplayHint.setStatus('current')
if mibBuilder.loadTexts: sliceColumnDisplayHint.setDescription("This defines how the data file will render this OID's value in the snapshot data file. The following subset of the C printf-style formatting macros is supported: %s - ascii string field %d - numeric field")
sliceAdminString = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 1, 1, 6), DisplayString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sliceAdminString.setStatus('current')
if mibBuilder.loadTexts: sliceAdminString.setDescription('Used for administrative purposes. Usually meaningful only to the controlling NMS.')
sliceEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: sliceEntryStatus.setStatus('current')
if mibBuilder.loadTexts: sliceEntryStatus.setDescription('The control variable that allows creation, modification, and deletion of entries in this table.')
xferTable = MibTable((1, 3, 6, 1, 3, 999, 2, 2), )
if mibBuilder.loadTexts: xferTable.setStatus('current')
if mibBuilder.loadTexts: xferTable.setDescription('This table describes a bulk data slice file transfer information. It is referenced when a snapshot is being requested.')
xferEntry = MibTableRow((1, 3, 6, 1, 3, 999, 2, 2, 1), ).setIndexNames((0, "BULK-DATA-MIB", "xferIndex"), (0, "BULK-DATA-MIB", "xferSubId"))
if mibBuilder.loadTexts: xferEntry.setStatus('current')
if mibBuilder.loadTexts: xferEntry.setDescription('The snapshot file transfer request table entry.')
xferIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: xferIndex.setStatus('current')
if mibBuilder.loadTexts: xferIndex.setDescription('An integer to uniquely identify a transfer destination set.')
xferSubId = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: xferSubId.setStatus('current')
if mibBuilder.loadTexts: xferSubId.setDescription('Sub index that allows several transfer entries to be grouped together to form a transfer set.')
xferHostIpType = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 2, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xferHostIpType.setStatus('current')
if mibBuilder.loadTexts: xferHostIpType.setDescription('Used along with xferHostIpAddr to define the IP address version.')
xferHostIpAddr = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 2, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xferHostIpAddr.setStatus('current')
if mibBuilder.loadTexts: xferHostIpAddr.setDescription('The IP address of the fileserver where the snapshot is to be transferred.')
xferProtocol = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cp", 1), ("ftp", 2), ("scp", 3))).clone('ftp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xferProtocol.setStatus('current')
if mibBuilder.loadTexts: xferProtocol.setDescription('This defines the standard protocol that is used to upload the snapshot to the fileserver. The agent is the client in this transaction; ie, it initiates the upload to the fileserver. When the snapshot is being kept on the local system, cp(1) is to be specified. For remote file transfers, ftp(2) or scp(3) should be specified.')
xferWriteControl = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("failIfExists", 1), ("overwrite", 2))).clone('failIfExists')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xferWriteControl.setStatus('current')
if mibBuilder.loadTexts: xferWriteControl.setDescription('This defines the action to take when uploading bulk data to a fileserver. If set to failIfExists(1) and a file already exists on the fileserver, the upload will fail and the existing file on the server will not be overwritten. If set to overwrite(2), a file will be uploaded and saved under the specified path and name even if one by that composite name already exists; if none exists by that composite name, a new file will be created.')
xferFilePath = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 2, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xferFilePath.setStatus('current')
if mibBuilder.loadTexts: xferFilePath.setDescription('The remote directory path where the file is to be saved on the fileserver.')
xferAuthUsername = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 2, 1, 8), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xferAuthUsername.setStatus('current')
if mibBuilder.loadTexts: xferAuthUsername.setDescription('The user name to use when authenticating with the remote fileserver.')
xferAuthPassword = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 2, 1, 9), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xferAuthPassword.setStatus('current')
if mibBuilder.loadTexts: xferAuthPassword.setDescription('The password to use when authenticating with the remote fileserver.')
xferAdminString = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 2, 1, 10), DisplayString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xferAdminString.setStatus('current')
if mibBuilder.loadTexts: xferAdminString.setDescription('Used for administrative purposes. Usually meaningful only to the controlling NMS.')
xferEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 2, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xferEntryStatus.setStatus('current')
if mibBuilder.loadTexts: xferEntryStatus.setDescription('The control that allows creation, modification, and deletion of entries. Setting this variable to createAndGo(4) or active(1) will case a row creation to be performed in this table. Note that no actual file transfer occurs until a snapshot table entry is created. Setting this variable to delete will delete this row entry.')
snapshotTable = MibTable((1, 3, 6, 1, 3, 999, 2, 3), )
if mibBuilder.loadTexts: snapshotTable.setStatus('current')
if mibBuilder.loadTexts: snapshotTable.setDescription('This table describes a bulk data slice snapshot request. The agent is expected to capture the values of the slice (atomically, if possible) and save them in a file on the local system when a row in this table is created and set to createAndGo(4) or active(1).')
snapshotEntry = MibTableRow((1, 3, 6, 1, 3, 999, 2, 3, 1), ).setIndexNames((0, "BULK-DATA-MIB", "snapshotIndex"), (0, "BULK-DATA-MIB", "snapshotSliceIndex"), (0, "BULK-DATA-MIB", "snapshotXferId"))
if mibBuilder.loadTexts: snapshotEntry.setStatus('current')
if mibBuilder.loadTexts: snapshotEntry.setDescription('The snapshot request table entry.')
snapshotIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: snapshotIndex.setStatus('current')
if mibBuilder.loadTexts: snapshotIndex.setDescription('An integer to uniquely identify the data slice that is to be transferred to the fileserver. This refers to an entry in the SliceTable.')
snapshotSliceIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: snapshotSliceIndex.setStatus('current')
if mibBuilder.loadTexts: snapshotSliceIndex.setDescription('An integer to uniquely identify the data slice to saved on the local system.')
snapshotXferId = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 3), Unsigned32())
if mibBuilder.loadTexts: snapshotXferId.setStatus('current')
if mibBuilder.loadTexts: snapshotXferId.setDescription('An instance in the xfer table that describes where and how to copy the bulk data snapshot to a fileserver.')
snapshotSnapFileName = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snapshotSnapFileName.setStatus('current')
if mibBuilder.loadTexts: snapshotSnapFileName.setDescription('The bulk data snapshot is saved under this filename.')
snapshotFileEncoding = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ascii", 1), ("xml", 2))).clone('ascii')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snapshotFileEncoding.setStatus('current')
if mibBuilder.loadTexts: snapshotFileEncoding.setDescription('If set to ascii(1), the format is human-readable ascii with a lines in the form: # timestampStart timestampCompletion col-1 col-2 ... col-n instance-1 value-1 value-2 ... instance-2 value-3 value-4 ... ... where: timestampStart and timestampCompletion are the values of sysUptime on the agent when the snapshot of the data slice was initiated and completed (with or without errors). column-1 thru column-n are the human-readable MIB module column names that are included in this data slice. instance-1 (etc) are human-readable MIB module instance names in usual dotted notation. value-1 (etc) are human-readable ascii representations of the actual values of the data cells. This is in DisplayString format regardless of the native data type of the column. It is implementation-specific if the column name is stored in dotted-OID format (.1.3.6...) or in symbolic format (ifInOctets). For example, an ifTable data slice file fragment might be: # 28711187 28711190 ifDescr ifType ifInOctets ifOutOctets 1 lo0 softwareLoopback 54550782 54552115 2 eth0 ethernet-csmacd 372380346 2746062289 3 eth0.0 ethernet-csmacd 4002949 126167 If set to xml(2), the data will be saved in XML tagged format.')
snapshotFileCompression = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noCompression", 1), ("bzip", 2), ("gzip", 3))).clone('noCompression')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snapshotFileCompression.setStatus('current')
if mibBuilder.loadTexts: snapshotFileCompression.setDescription('If set to noCompression(1), no file compression will be applied before the data slice is transferred to the fileserver. If set to bzip(2), the standard bzip compression algorithm will be applied to the data slice before the file is uploaded to the fileserver. If set to gzip(3), the standard GNU gzip compression algorithm will be applied to the data slice before the file is uploaded to the fileserver.')
snapshotStartTime = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapshotStartTime.setStatus('current')
if mibBuilder.loadTexts: snapshotStartTime.setDescription('The value of sysUptime on the agent when the snapshot was initiated.')
snapshotCompletionTime = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapshotCompletionTime.setStatus('current')
if mibBuilder.loadTexts: snapshotCompletionTime.setDescription('The value of sysUptime on the agent when the snapshot was completed (with or without an error).')
snapshotFileSize = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapshotFileSize.setStatus('current')
if mibBuilder.loadTexts: snapshotFileSize.setDescription('The actual size of the file (after optional file compression was applied) at the completion of the snapshot. The size is measured in bytes. This variable is only valid upon the successful completion of a slice snapshot.')
snapshotState = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("running", 1), ("ready", 2), ("noSpace", 3), ("badName", 4), ("writeErr", 5), ("noMem", 6), ("aborted", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snapshotState.setStatus('current')
if mibBuilder.loadTexts: snapshotState.setDescription("The file state: running data is being written to the file ready the file is ready to be sent or retrieved noSpace no data due to insufficient file space badName no data due to a name or path problem writeErr no data due to fatal file write error noMem no data due to insufficient dynamic memory aborted terminated by operator command Only the 'ready' state implies that snapshot has successfully completed.")
snapshotAdminString = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 11), DisplayString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snapshotAdminString.setStatus('current')
if mibBuilder.loadTexts: snapshotAdminString.setDescription('Used for administrative purposes. Usually meaningful only to the controlling NMS.')
snapshotEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 3, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snapshotEntryStatus.setStatus('current')
if mibBuilder.loadTexts: snapshotEntryStatus.setDescription("The control that allows creation, modification, and deletion of entries. Setting this variable to createAndGo(4) or active(1) will initiate a snapshot of a slice entry to the local system and optionally initiate a remote file copy. Setting this variable to delete() will delete this row entry and delete the corresponding data file on the local system. Note that in practice, this variable could be set by an operator via the agent's craft interface, remotely via an NMS using SNMP or locally within the agent via automatic means, such as described in the DISMAN-SCHEDULE-MIB.")
xferCtlTable = MibTable((1, 3, 6, 1, 3, 999, 2, 4), )
if mibBuilder.loadTexts: xferCtlTable.setStatus('current')
if mibBuilder.loadTexts: xferCtlTable.setDescription('This table contains individual (fileserver host) transfer requests. There will be an entry in this table For each filserver that is to receive a snapshot slice. The current transfer status can be monitored as well as controlled (aborted, retried).')
xferCtlEntry = MibTableRow((1, 3, 6, 1, 3, 999, 2, 4, 1), ).setIndexNames((0, "BULK-DATA-MIB", "xferCtlIndex"), (0, "BULK-DATA-MIB", "sliceIndex"), (0, "BULK-DATA-MIB", "xferIndex"), (0, "BULK-DATA-MIB", "xferSubId"))
if mibBuilder.loadTexts: xferCtlEntry.setStatus('current')
if mibBuilder.loadTexts: xferCtlEntry.setDescription('The snapshot file transfer request table entry.')
xferCtlIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: xferCtlIndex.setStatus('current')
if mibBuilder.loadTexts: xferCtlIndex.setDescription('An integer to uniquely identify a transfer destination set.')
xferCtlStartTime = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 4, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferCtlStartTime.setStatus('current')
if mibBuilder.loadTexts: xferCtlStartTime.setDescription('The value of sysUptime on the agent when the file transfer was initiated.')
xferCtlCompletionTime = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 4, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferCtlCompletionTime.setStatus('current')
if mibBuilder.loadTexts: xferCtlCompletionTime.setDescription('The value of sysUptime on the agent when the file transfer was completed (with or without an error).')
xferCtlPercentXferred = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xferCtlPercentXferred.setStatus('current')
if mibBuilder.loadTexts: xferCtlPercentXferred.setDescription('The amount of the snapshot file that has been transferred to the fileserver, in percent of completion (0..100).')
xferCtlStatus = MibTableColumn((1, 3, 6, 1, 3, 999, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("inProgress", 1), ("complete", 2), ("noSpace", 3), ("badName", 4), ("writeErr", 5), ("badLogin", 6), ("abortXfer", 7), ("retryXfer", 8), ("deleteRow", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xferCtlStatus.setStatus('current')
if mibBuilder.loadTexts: xferCtlStatus.setDescription('This allows individual file transfer requests to be controlled. inProgress(1) is returned if a file transfer is currently being performed by the local system. This is a read-only value. complete(2) is returned upon successful file transfer. This is a read-only value. noSpace(3), badName(4), writeErr(5), badLogin(6) are error status values that describe the error conditions of insufficient fileserver space to create the file, invalid filename, misc write error or authentication error on the fileserver. These values are readable but not writable. abortXfer(7), retryXfer(8) are writable values and allow remote control of currently pending file transfer requests. deleteRow(9) is a writable value that causes a row deletion from this table. In addition, any pending operations on this row are aborted.')
bulkDataXfer = NotificationType((1, 3, 6, 1, 3, 999, 3, 1)).setObjects(("BULK-DATA-MIB", "xferCtlStatus"))
if mibBuilder.loadTexts: bulkDataXfer.setStatus('current')
if mibBuilder.loadTexts: bulkDataXfer.setDescription('Asynchronous events that are sent when a file transfer request changes state.')
bulkMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 999, 4))
bulkMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 999, 4, 1))
bulkMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 999, 4, 2))
bulkMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 999, 4, 1, 1)).setObjects(("BULK-DATA-MIB", "bulkCapabilitiesGroup"), ("BULK-DATA-MIB", "bulkSliceGroup"), ("BULK-DATA-MIB", "bulkFileTransferGroup"), ("BULK-DATA-MIB", "bulkSnapshotGroup"), ("BULK-DATA-MIB", "bulkXferCtlGroup"), ("BULK-DATA-MIB", "bulkTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bulkMIBCompliance = bulkMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: bulkMIBCompliance.setDescription('The compliance statement for entities which implement the Bulk Data MIB. Implementation of this MIB is based on individual product needs.')
bulkCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 3, 999, 4, 2, 1)).setObjects(("BULK-DATA-MIB", "acFileEncoding"), ("BULK-DATA-MIB", "acFileCompression"), ("BULK-DATA-MIB", "acXferProtocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bulkCapabilitiesGroup = bulkCapabilitiesGroup.setStatus('current')
if mibBuilder.loadTexts: bulkCapabilitiesGroup.setDescription('Bulk Data agent capabilities management.')
bulkSliceGroup = ObjectGroup((1, 3, 6, 1, 3, 999, 4, 2, 2)).setObjects(("BULK-DATA-MIB", "sliceColumnOID"), ("BULK-DATA-MIB", "sliceSnmpContext"), ("BULK-DATA-MIB", "sliceColumnDisplayHint"), ("BULK-DATA-MIB", "sliceAdminString"), ("BULK-DATA-MIB", "sliceEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bulkSliceGroup = bulkSliceGroup.setStatus('current')
if mibBuilder.loadTexts: bulkSliceGroup.setDescription('Bulk Data slice management.')
bulkFileTransferGroup = ObjectGroup((1, 3, 6, 1, 3, 999, 4, 2, 3)).setObjects(("BULK-DATA-MIB", "xferHostIpType"), ("BULK-DATA-MIB", "xferHostIpAddr"), ("BULK-DATA-MIB", "xferProtocol"), ("BULK-DATA-MIB", "xferWriteControl"), ("BULK-DATA-MIB", "xferFilePath"), ("BULK-DATA-MIB", "xferAuthUsername"), ("BULK-DATA-MIB", "xferAuthPassword"), ("BULK-DATA-MIB", "xferAdminString"), ("BULK-DATA-MIB", "xferEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bulkFileTransferGroup = bulkFileTransferGroup.setStatus('current')
if mibBuilder.loadTexts: bulkFileTransferGroup.setDescription('Bulk File transfer management.')
bulkSnapshotGroup = ObjectGroup((1, 3, 6, 1, 3, 999, 4, 2, 4)).setObjects(("BULK-DATA-MIB", "snapshotSnapFileName"), ("BULK-DATA-MIB", "snapshotFileEncoding"), ("BULK-DATA-MIB", "snapshotFileCompression"), ("BULK-DATA-MIB", "snapshotStartTime"), ("BULK-DATA-MIB", "snapshotCompletionTime"), ("BULK-DATA-MIB", "snapshotFileSize"), ("BULK-DATA-MIB", "snapshotState"), ("BULK-DATA-MIB", "snapshotAdminString"), ("BULK-DATA-MIB", "snapshotEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bulkSnapshotGroup = bulkSnapshotGroup.setStatus('current')
if mibBuilder.loadTexts: bulkSnapshotGroup.setDescription('Bulk data snapshot management.')
bulkXferCtlGroup = ObjectGroup((1, 3, 6, 1, 3, 999, 4, 2, 5)).setObjects(("BULK-DATA-MIB", "xferCtlStartTime"), ("BULK-DATA-MIB", "xferCtlCompletionTime"), ("BULK-DATA-MIB", "xferCtlPercentXferred"), ("BULK-DATA-MIB", "xferCtlStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bulkXferCtlGroup = bulkXferCtlGroup.setStatus('current')
if mibBuilder.loadTexts: bulkXferCtlGroup.setDescription('Bulk Data transfer control management.')
bulkTrapGroup = NotificationGroup((1, 3, 6, 1, 3, 999, 4, 2, 6)).setObjects(("BULK-DATA-MIB", "bulkDataXfer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bulkTrapGroup = bulkTrapGroup.setStatus('current')
if mibBuilder.loadTexts: bulkTrapGroup.setDescription('Bulk Data trap management.')
mibBuilder.exportSymbols("BULK-DATA-MIB", snapshotFileSize=snapshotFileSize, xferCtlPercentXferred=xferCtlPercentXferred, bulkDataObjects=bulkDataObjects, bulkMIBCompliances=bulkMIBCompliances, xferIndex=xferIndex, bulkDataMIB=bulkDataMIB, bulkMIBGroups=bulkMIBGroups, xferSubId=xferSubId, snapshotEntryStatus=snapshotEntryStatus, xferAuthUsername=xferAuthUsername, snapshotSnapFileName=snapshotSnapFileName, sliceSnmpContext=sliceSnmpContext, xferEntry=xferEntry, sliceAdminString=sliceAdminString, sliceColumnDisplayHint=sliceColumnDisplayHint, xferAdminString=xferAdminString, xferEntryStatus=xferEntryStatus, snapshotAdminString=snapshotAdminString, sliceTable=sliceTable, xferHostIpType=xferHostIpType, xferCtlStartTime=xferCtlStartTime, snapshotXferId=snapshotXferId, snapshotFileEncoding=snapshotFileEncoding, snapshotCompletionTime=snapshotCompletionTime, snapshotState=snapshotState, xferWriteControl=xferWriteControl, xferCtlIndex=xferCtlIndex, xferFilePath=xferFilePath, bulkSnapshotGroup=bulkSnapshotGroup, xferHostIpAddr=xferHostIpAddr, xferCtlTable=xferCtlTable, sliceSubId=sliceSubId, xferCtlStatus=xferCtlStatus, xferTable=xferTable, bulkFileTransferGroup=bulkFileTransferGroup, snapshotStartTime=snapshotStartTime, bulkMIBConformance=bulkMIBConformance, snapshotFileCompression=snapshotFileCompression, xferCtlEntry=xferCtlEntry, bulkDataXfer=bulkDataXfer, snapshotEntry=snapshotEntry, snapshotTable=snapshotTable, sliceIndex=sliceIndex, acFileEncoding=acFileEncoding, sliceEntryStatus=sliceEntryStatus, bulkSliceGroup=bulkSliceGroup, xferAuthPassword=xferAuthPassword, xferCtlCompletionTime=xferCtlCompletionTime, sliceEntry=sliceEntry, acXferProtocol=acXferProtocol, xferProtocol=xferProtocol, sliceColumnOID=sliceColumnOID, snapshotIndex=snapshotIndex, bulkMIBCompliance=bulkMIBCompliance, bulkTrapGroup=bulkTrapGroup, snapshotSliceIndex=snapshotSliceIndex, bulkXferCtlGroup=bulkXferCtlGroup, bulkDataTraps=bulkDataTraps, acFileCompression=acFileCompression, bulkCapabilitiesGroup=bulkCapabilitiesGroup, PYSNMP_MODULE_ID=bulkDataMIB, bulkDataAgentCapabilities=bulkDataAgentCapabilities)
