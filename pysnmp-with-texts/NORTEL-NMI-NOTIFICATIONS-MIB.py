#
# PySNMP MIB module NORTEL-NMI-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NORTEL-NMI-NOTIFICATIONS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nortelNetworkManagementInterfaceMIBs, = mibBuilder.importSymbols("NORTEL-GENERIC-MIB", "nortelNetworkManagementInterfaceMIBs")
NortelNMIoperState, NortelNMIunknownStatusValue, NortelNMIneType, NortelNMIadminState = mibBuilder.importSymbols("NORTEL-NMI-TC-MIB", "NortelNMIoperState", "NortelNMIunknownStatusValue", "NortelNMIneType", "NortelNMIadminState")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, iso, IpAddress, Integer32, Gauge32, TimeTicks, ObjectIdentity, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "iso", "IpAddress", "Integer32", "Gauge32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nortelNMInotificationsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 6))
nortelNMInotificationsMIB.setRevisions(('1999-07-19 00:00', '1999-06-24 00:00', '1999-05-31 00:00', '1999-04-12 00:00', '1999-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nortelNMInotificationsMIB.setRevisionsDescriptions(('Add ASCII string limitations for NE name / componentID, etc.', ' The fourth version of this MIB module. Module-identity oid assignment changed. Revisions introduced by Shobana Sundaram.', ' The third version of this MIB module. Contact info updated and Revision history added. Revisions introduced by Shobana Sundaram.', ' The second version of this MIB module. Contact info updated and Revision history added.', ' The first version of this MIB module.',))
if mibBuilder.loadTexts: nortelNMInotificationsMIB.setLastUpdated('9907190000Z')
if mibBuilder.loadTexts: nortelNMInotificationsMIB.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: nortelNMInotificationsMIB.setContactInfo(' Jingdong Liu Postal: Nortel Networks P. O. Box 3511, Station C Ottawa, Ontario CANADA K1Y 4H7 Email: jingdong@nortelnetworks.com')
if mibBuilder.loadTexts: nortelNMInotificationsMIB.setDescription('This module contains the notification branches for the Nortel NMI along with the definition of the notification sequence number variable.')
nortelNMIcurrentTxNotificationSequenceNum = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nortelNMIcurrentTxNotificationSequenceNum.setStatus('current')
if mibBuilder.loadTexts: nortelNMIcurrentTxNotificationSequenceNum.setDescription('This variable represents the sequence number of the Notifications and is incremented by one whenever a notification is emitted from the agent. This would be included as a varbind for all notifications and this value when read indicates the sequence number of the last transmitted trap. ')
nortelNMIcommonNotiVarbinds = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2))
if mibBuilder.loadTexts: nortelNMIcommonNotiVarbinds.setStatus('current')
if mibBuilder.loadTexts: nortelNMIcommonNotiVarbinds.setDescription('This OID represents the branch for varbinds that are common to all categories of Nortel NMI Notifications.')
nortelNMIconfigNotiMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3))
if mibBuilder.loadTexts: nortelNMIconfigNotiMIB.setStatus('current')
if mibBuilder.loadTexts: nortelNMIconfigNotiMIB.setDescription('This OID represents the branch for all configuration related Nortel NMI Notifications.')
nortelNMIfaultNotiMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4))
if mibBuilder.loadTexts: nortelNMIfaultNotiMIB.setStatus('current')
if mibBuilder.loadTexts: nortelNMIfaultNotiMIB.setDescription('This OID represents the branch for all fault management related Nortel NMI Notifications.')
nortelNMIinfoNotiMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5))
if mibBuilder.loadTexts: nortelNMIinfoNotiMIB.setStatus('current')
if mibBuilder.loadTexts: nortelNMIinfoNotiMIB.setDescription('This OID represents the branch for all informational log related Nortel NMI Notifications.')
nortelNMInotifyNeType = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2, 1), NortelNMIneType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyNeType.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyNeType.setDescription('This variable represents the type of the NE that is being enrolled into the network management domain. NortelNMIneType textual convention is defined at the NORTEL-NMI-TC-MIB.')
nortelNMInotifyNeName = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyNeName.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyNeName.setDescription('This variable represents the name of the NE that is being enrolled into the network management domain. This name should uniquely identify the NE in the EMS domain across all NE types. The NeName string should be a single word, can only contain alphanumeric characters and underscores. No commas, spaces, slashes, hyphens, or dollar signs is allowed.')
nortelNMInotifyNeAdminState = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2, 3), NortelNMIadminState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyNeAdminState.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyNeAdminState.setDescription('This variable presents the administratively assigned state (ITU-T X.731) of the NE. The textual convention NortelNMIadminState defined at NORTEL-NMI-TC-MIB.')
nortelNMInotifyNeOperState = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2, 4), NortelNMIoperState()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyNeOperState.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyNeOperState.setDescription('This variable presents the current operational state (ITU-T X.731) of the NE.')
nortelNMInotifyNeUnknownStatus = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 2, 5), NortelNMIunknownStatusValue()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyNeUnknownStatus.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotifyNeUnknownStatus.setDescription('This variable presents the NE unknown Status Values as per (ITU-T X.731). The textual convention NortelNMIunknownStatusValue defined at NORTEL-NMI-TC-MIB is of type Truthvalue (SNMPv2-TC).')
mibBuilder.exportSymbols("NORTEL-NMI-NOTIFICATIONS-MIB", nortelNMIcommonNotiVarbinds=nortelNMIcommonNotiVarbinds, nortelNMIinfoNotiMIB=nortelNMIinfoNotiMIB, PYSNMP_MODULE_ID=nortelNMInotificationsMIB, nortelNMInotificationsMIB=nortelNMInotificationsMIB, nortelNMInotifyNeType=nortelNMInotifyNeType, nortelNMIfaultNotiMIB=nortelNMIfaultNotiMIB, nortelNMInotifyNeAdminState=nortelNMInotifyNeAdminState, nortelNMInotifyNeUnknownStatus=nortelNMInotifyNeUnknownStatus, nortelNMIconfigNotiMIB=nortelNMIconfigNotiMIB, nortelNMInotifyNeName=nortelNMInotifyNeName, nortelNMInotifyNeOperState=nortelNMInotifyNeOperState, nortelNMIcurrentTxNotificationSequenceNum=nortelNMIcurrentTxNotificationSequenceNum)
