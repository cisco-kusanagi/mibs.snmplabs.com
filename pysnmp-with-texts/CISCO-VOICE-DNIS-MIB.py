#
# PySNMP MIB module CISCO-VOICE-DNIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-DNIS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, iso, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Unsigned32, ModuleIdentity, ObjectIdentity, IpAddress, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "iso", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Gauge32", "MibIdentifier")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
ciscoVoiceDnisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 219))
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setLastUpdated('200205010000Z')
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setDescription('The MIB module provides management support for Dialer Number Information Service (DNIS) mapping. A DNIS entry is associated with a Voice XML (VXML) page to provide audio play back features. Multiple DNIS entries can be grouped together to form a DNIS mapping with a unique map name. *** ABBREVIATIONS, ACRONYMS, AND SYMBOLS *** DNIS - Dialer Number Information Service XML - Extensible Markup Language VXML - Voice XML URL - Uniform Resource Locator ')
class DnisMapname(TextualConvention, OctetString):
    description = 'An identification for a DNIS map name or a DNIS name. A DNIS map name correspods to a group of individual DNIS names. The DNIS map names are unique in the system, and within each map name, individual DNIS names are unique. '
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvE164String(TextualConvention, OctetString):
    description = "A UTF-8 string limited to the character set defined for E.164, '0123456789*#,<quote>'. Note that <quote> represents the double quote which cannot be contained in a SMI description clause."
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

cvDnisMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 1))
cvDnisMap = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1))
cvDnisMappingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1), )
if mibBuilder.loadTexts: cvDnisMappingTable.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingTable.setDescription('The table contains the map name and a url specifying a file name. The file contains DNIS entries that belong to the DNIS mapping. ')
cvDnisMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1), ).setIndexNames((1, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"))
if mibBuilder.loadTexts: cvDnisMappingEntry.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingEntry.setDescription('Information about a single DNIS mapping. There is a unique DNIS map name. New DNIS mapping can be created using cvDnisMappingStatus. The entry can be created with or without a file location specified by cvDnisMappingUrl. The mapping file contains DNIS name and VXML page per line. For example, a cvDnisMappingUrl could be tftp://someserver/dnismap.txt. This file is a text file and the content format is dnis <dnisname> url <urlname>. An example of the contents of the file itself can be dnis 18004251234 url http://www.b.com/p/vwelcome.vxml dnis 18004253421 url http://www.c.com/j/vxmlintf.vxml If a mapping file location is specified, then new rows corresponding to this map name are created and populated in cvDnisNodeTable from the contents of the file. The rows corresponding to this map name in cvDnisNodeTable cannot be created or modified or deleted but can be read. If a mapping file location is not specified in cvDnisMappingUrl, then individual DNIS entries corresponding to this map name can be created, modified and deleted in cvDnisNodeTable. Deleting an entry deletes all the related entries in cvDnisNodeTable. ')
cvDnisMappingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 1), DnisMapname().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cvDnisMappingName.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingName.setDescription('The name which uniquely identifies a DNIS mapping. ')
cvDnisMappingUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingUrl.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingUrl.setDescription('The url specifies a file location. The file contains individual DNIS entries that belong to the DNIS map name specified by cvDnisMappingName. Once a url is created and associated with a map name (the association is complete when the row is made active(1)), it cannot be modified while cvDnisMappingStatus is active. If a different url needs to be associated with the current map name, the row status should be made notInService(2) and this object has to be modified to associate a new url. When a new association is made all the DNIS entries corresponding to the old association will be deleted from the cvDnisNodeTable. The url is read when the row status is made active(1) or when the row status is active and the object cvDnisMappingRefresh is explicitly set to refresh(2). If the url is not accessible then a cvDnisMappingUrlInaccessible notification will be generted. ')
cvDnisMappingRefresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("refresh", 2))).clone('idle')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingRefresh.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingRefresh.setDescription('Whenever there is a need to re-read the contents of the file specified by cvDnisMappingUrl, this object can be set to refresh(2). This will cause the contents of the file to be re-read and correspondingly update the cvDnisNodeTable. After the completion of this operation, the value of this object is reset to idle(1). The only operation allowed on this object is setting it to refresh(2). This can only be done when the current value is idle(1) and the rowstatus is active(1). idle - The refreshing process is idle and the user can modify this object to refresh. refresh - The refreshing process is currently busy and the user have to wait till the object becomes idle to issue new refresh. ')
cvDnisMappingUrlAccessError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvDnisMappingUrlAccessError.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingUrlAccessError.setDescription('ASCII text describing the error on last access of the url specified in cvDnisMappingUrl. If the url access does not succeed, then this object is populated with an error message indicating the reason for failure. If the url access succeeds, this object is set to null string. ')
cvDnisMappingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingStatus.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table. When making the status active(1), if a valid cvDnisMappingUrl is present the contents of the url is downloaded and during that time cvDnisMappingRefresh is set to refresh(2). When cvDnisMappingRefresh is set to refresh(2), only the destroy(6) operation is allowed. ')
cvDnisNodeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2), )
if mibBuilder.loadTexts: cvDnisNodeTable.setStatus('current')
if mibBuilder.loadTexts: cvDnisNodeTable.setDescription('The table contains a DNIS name and a url. The url is a pointer to a VXML page for the DNIS name. ')
cvDnisNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"), (1, "CISCO-VOICE-DNIS-MIB", "cvDnisNumber"))
if mibBuilder.loadTexts: cvDnisNodeEntry.setStatus('current')
if mibBuilder.loadTexts: cvDnisNodeEntry.setDescription("Each entry is a DNIS name and the location of the associated VXML page. New DNIS entries can be created or the existing entries can be modified or deleted only if the corresponding map name (defined in cvDnisMappingTable) does not have any file name provided in the cvDnisMappingUrl object. If a file name is provided in cvDnisMappingUrl corresponding to this entry's map name, then this row will have read permission only. ")
cvDnisNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 1), CvE164String())
if mibBuilder.loadTexts: cvDnisNumber.setStatus('current')
if mibBuilder.loadTexts: cvDnisNumber.setDescription('The individual DNIS name. It is unique within a DNIS mapping. ')
cvDnisNodeUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisNodeUrl.setStatus('current')
if mibBuilder.loadTexts: cvDnisNodeUrl.setDescription('The url specifies a VXML page. This page contains voice XML links to play audio data. This url which is a VXML page is not read immediately when the row is made active(1), but only when a call that requires the use of this DNIS comes through. ')
cvDnisNodeModifiable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvDnisNodeModifiable.setStatus('current')
if mibBuilder.loadTexts: cvDnisNodeModifiable.setDescription('This object specifies whether the object in a particular row is modifiable. The object is set to true(1) if the corresponding map name (defined in cvDnisMappingTable) does not have any file name provided in the cvDnisMappingUrl object. Otherwise this object is set to false(2) and the row becomes read only. ')
cvDnisNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisNodeStatus.setStatus('current')
if mibBuilder.loadTexts: cvDnisNodeStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table. The objects in a row can be modified or deleted while the row status is active(1) and cvDnisNodeModifiable is true(1). The row status cannot be set to notInService(2) or createAndWait(5). ')
cvDnisMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 2))
cvDnisMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0))
cvDnisMappingUrlInaccessible = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"))
if mibBuilder.loadTexts: cvDnisMappingUrlInaccessible.setStatus('current')
if mibBuilder.loadTexts: cvDnisMappingUrlInaccessible.setDescription('Inaccessible DNIS mapping url notification. A cvDnisMappingUrlInaccessible notification is sent if the specified url is not accessible. ')
cvDnisMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3))
cvDnisMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1))
cvDnisMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2))
cvDnisMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisGroup"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisMIBCompliance = cvDnisMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvDnisMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO VOICE DNIS MIB')
cvDnisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingRefresh"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingStatus"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeModifiable"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisGroup = cvDnisGroup.setStatus('current')
if mibBuilder.loadTexts: cvDnisGroup.setDescription('A collection of objects provides a relation between a DNIS map name and the DNIS entries belonging to that map name. ')
cvDnisNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 2)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlInaccessible"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisNotificationGroup = cvDnisNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cvDnisNotificationGroup.setDescription('The notifications for CISCO-VOICE-DNIS-MIB. ')
mibBuilder.exportSymbols("CISCO-VOICE-DNIS-MIB", cvDnisMappingTable=cvDnisMappingTable, cvDnisNodeUrl=cvDnisNodeUrl, ciscoVoiceDnisMIB=ciscoVoiceDnisMIB, cvDnisMappingUrlInaccessible=cvDnisMappingUrlInaccessible, cvDnisMIBGroups=cvDnisMIBGroups, cvDnisNotificationGroup=cvDnisNotificationGroup, cvDnisNodeTable=cvDnisNodeTable, cvDnisGroup=cvDnisGroup, cvDnisMIBObjects=cvDnisMIBObjects, cvDnisMap=cvDnisMap, cvDnisMIBCompliances=cvDnisMIBCompliances, PYSNMP_MODULE_ID=ciscoVoiceDnisMIB, cvDnisMappingName=cvDnisMappingName, cvDnisMappingUrl=cvDnisMappingUrl, cvDnisMappingStatus=cvDnisMappingStatus, cvDnisNumber=cvDnisNumber, CvE164String=CvE164String, cvDnisMIBConformance=cvDnisMIBConformance, DnisMapname=DnisMapname, cvDnisMappingRefresh=cvDnisMappingRefresh, cvDnisNodeModifiable=cvDnisNodeModifiable, cvDnisMIBNotifications=cvDnisMIBNotifications, cvDnisNodeEntry=cvDnisNodeEntry, cvDnisMappingUrlAccessError=cvDnisMappingUrlAccessError, cvDnisMIBNotificationPrefix=cvDnisMIBNotificationPrefix, cvDnisNodeStatus=cvDnisNodeStatus, cvDnisMIBCompliance=cvDnisMIBCompliance, cvDnisMappingEntry=cvDnisMappingEntry)
