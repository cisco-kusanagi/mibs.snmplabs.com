#
# PySNMP MIB module ARISTA-CONFIG-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-CONFIG-COPY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:24:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, aristaProducts, aristaModules = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs", "aristaProducts", "aristaModules")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, ObjectIdentity, Unsigned32, Counter32, TimeTicks, NotificationType, IpAddress, iso, MibIdentifier, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Counter32", "TimeTicks", "NotificationType", "IpAddress", "iso", "MibIdentifier", "Gauge32", "Integer32")
DateAndTime, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "RowStatus", "TextualConvention")
aristaConfigCopyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 7))
aristaConfigCopyMIB.setRevisions(('2014-08-15 00:00', '2013-02-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaConfigCopyMIB.setRevisionsDescriptions(('Updated postal and e-mail addresses.', 'The initial revision of this MIB module.',))
if mibBuilder.loadTexts: aristaConfigCopyMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaConfigCopyMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaConfigCopyMIB.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaConfigCopyMIB.setDescription('This MIB is for copying a source URI to a destination URI. A URI specifies the location of a local file, network file, running-config or startup-config. The resources specified by the URIs are copied from/to Arista devices. Currently supported URI schemes include: file, flash, extension, system, ftp, http, https and tftp.')
class ConfigCopyState(TextualConvention, Integer32):
    description = 'The state of a copy request. Here are the possible states: inactive: no copy request has been queued yet. This is the default state when a row is created. scheduled: the copy request has been scheduled to run, but has not started yet (probably waiting for ealier copy requests to complete). running: the copy request has been started. completed: the copy request is completed with success. failed: the copy request failed (probably because network problem, timeout, permission denial, etc.) Once the row is activated, the agent will mark the row as scheduled. It changes state to running when the copy request is started. Once the copy request is completed, the state changes to completed or failed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("inactive", 0), ("scheduled", 1), ("running", 2), ("completed", 3), ("failed", 4))

class ConfigCopyFailureCause(TextualConvention, Integer32):
    description = 'The reason why a copy request failed. Possible causes are: none: the copy request succeeded. unknown: the copy request failed without a clear cause, details are in the failure message. timeout: the copy request took too long and has been terminated.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("unknown", 1), ("timeout", 2))

aristaConfigCopyCommandTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1), )
if mibBuilder.loadTexts: aristaConfigCopyCommandTable.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyCommandTable.setDescription('A table of copy requests. Each row corresponds to a copy request. The completed rows are accessible for status retrival for a certain peroid of time and then will be gradually aged out by the agent.')
aristaConfigCopyCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1), ).setIndexNames((0, "ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyName"), (0, "ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyId"))
if mibBuilder.loadTexts: aristaConfigCopyCommandEntry.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyCommandEntry.setDescription('A copy request. A management station should generate a unique ID and name (as the index) for each copy request. This prevents multiple management stations or applications from using same index and causing conflicts in same row. After an unique index is generated, the management station could create a row with that index and setup a copy request. Once a copy request is setup correctly with both source and destination URIs, it can be queued by setting the row status to active. The row creation, copy request setup and row activation can be done in one or multiple SET requests. The status of the copy request may change after the request is queued. It can be retrieved at any time before the request is aged out by the agent. ')
aristaConfigCopyName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: aristaConfigCopyName.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyName.setDescription('The name of a copy request. It is chosen by the management station and should be unique so that two management stations or applications do not cause conflicts in same row.')
aristaConfigCopyId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: aristaConfigCopyId.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyId.setDescription('The ID of a copy request. It is chosen by the management station and should be unique. One way to generate such a unique intenger is through the TestAndIncr mechanism (in SNMPv2-TC).')
aristaConfigCopySourceUri = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopySourceUri.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopySourceUri.setDescription('The source URI of a copy request. The URI format is: scheme://[username:password@]host/path Supported URI schemes are: file, flash, extension, system, ftp, http, https and tftp. username and password may be required for a network URI scheme (e.g. ftp). For convenience, two aliases are supported: startup-config -> flash://startup-config running-config -> system://running-config ')
aristaConfigCopyDestUri = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopyDestUri.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyDestUri.setDescription('The destination URI of a copy request. It has the same format as the source URI.')
aristaConfigCopyState = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 5), ConfigCopyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyState.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyState.setDescription('The state of a copy request.')
aristaConfigCopyTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 6), Unsigned32().clone(60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopyTimeout.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyTimeout.setDescription('The maximum number of seconds a copy request could run. If the copy request is not completed in such amount of time, it will be terminated and marked as failed with a failure cause of timeout. The time taken by a copy request varies by the source and/ or destination file size, network condition, system load, etc. A reasonable timeout should be chosen so that a stuck or run-away copy request could be terminated, but a normal copy request could complete.')
aristaConfigCopyTimeStarted = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyTimeStarted.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyTimeStarted.setDescription('The time when a copy request was started.')
aristaConfigCopyTimeCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyTimeCompleted.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyTimeCompleted.setDescription('The time when a copy request was completed.')
aristaConfigCopyFailureCause = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 9), ConfigCopyFailureCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyFailureCause.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyFailureCause.setDescription('The cause of a failed copy request.')
aristaConfigCopyFailureMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyFailureMessage.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyFailureMessage.setDescription('The details of a failed copy request.')
aristaConfigCopyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopyRowStatus.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyRowStatus.setDescription('The row status of a copy request. A new copy request is instantiated by creating a new row. An existing copy request is queued by activating a row, or cancelled by destroying a row.')
aristaConfigCopyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2))
aristaConfigCopyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 1))
aristaConfigCopyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 2))
aristaConfigCopyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 1, 1)).setObjects(("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigCopyCompliance = aristaConfigCopyCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyCompliance.setDescription('The compliance statement for SNMP entities which implement the ARISTA-CONFIG-COPY-MIB.')
aristaConfigCopyObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 2, 1)).setObjects(("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopySourceUri"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyDestUri"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyState"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeout"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeStarted"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeCompleted"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyFailureCause"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyFailureMessage"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigCopyObjectsGroup = aristaConfigCopyObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: aristaConfigCopyObjectsGroup.setDescription('The collection of objects in the ARISTA-CONFIG-COPY-MIB.')
mibBuilder.exportSymbols("ARISTA-CONFIG-COPY-MIB", aristaConfigCopyCommandTable=aristaConfigCopyCommandTable, aristaConfigCopyState=aristaConfigCopyState, aristaConfigCopyRowStatus=aristaConfigCopyRowStatus, PYSNMP_MODULE_ID=aristaConfigCopyMIB, aristaConfigCopyObjectsGroup=aristaConfigCopyObjectsGroup, ConfigCopyFailureCause=ConfigCopyFailureCause, aristaConfigCopyCommandEntry=aristaConfigCopyCommandEntry, aristaConfigCopyTimeCompleted=aristaConfigCopyTimeCompleted, aristaConfigCopyMIB=aristaConfigCopyMIB, aristaConfigCopyCompliances=aristaConfigCopyCompliances, ConfigCopyState=ConfigCopyState, aristaConfigCopyFailureCause=aristaConfigCopyFailureCause, aristaConfigCopyDestUri=aristaConfigCopyDestUri, aristaConfigCopySourceUri=aristaConfigCopySourceUri, aristaConfigCopyFailureMessage=aristaConfigCopyFailureMessage, aristaConfigCopyName=aristaConfigCopyName, aristaConfigCopyTimeout=aristaConfigCopyTimeout, aristaConfigCopyId=aristaConfigCopyId, aristaConfigCopyTimeStarted=aristaConfigCopyTimeStarted, aristaConfigCopyGroups=aristaConfigCopyGroups, aristaConfigCopyCompliance=aristaConfigCopyCompliance, aristaConfigCopyConformance=aristaConfigCopyConformance)
