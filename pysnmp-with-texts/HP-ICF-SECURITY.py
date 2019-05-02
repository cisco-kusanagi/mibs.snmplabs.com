#
# PySNMP MIB module HP-ICF-SECURITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-SECURITY
# Produced by pysmi-0.3.4 at Wed May  1 13:35:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
icfSecurity, hpicfObjectModules = mibBuilder.importSymbols("HP-ICF-OID", "icfSecurity", "hpicfObjectModules")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, iso, MibIdentifier, NotificationType, Counter64, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, IpAddress, ObjectIdentity, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "MibIdentifier", "NotificationType", "Counter64", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "IpAddress", "ObjectIdentity", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
icfSecurityMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1))
icfSecurityMib.setRevisions(('2008-03-05 09:00', '2007-10-01 09:03', '2003-01-09 01:12', '2000-11-03 07:56', '1996-09-10 02:00', '1996-01-25 03:56', '1993-07-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: icfSecurityMib.setRevisionsDescriptions(('Added icfAuthIPMgrAccessMethod.', 'Deprecated icfAuthIPMgrAddress and icfAuthIPMgrMask.', 'Deprecated icfCommunityTable and icfAuthMgrTable.', 'Added icfAuthIPMgrTable. Updated division name.', 'Updated division name in ORGANIZATION clause.', 'Split this MIB module from the former monolithic hp-icf MIB. Added the SNMP community group.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: icfSecurityMib.setLastUpdated('200803050900Z')
if mibBuilder.loadTexts: icfSecurityMib.setOrganization('HP Networking')
if mibBuilder.loadTexts: icfSecurityMib.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: icfSecurityMib.setDescription('This MIB module describes objects for managing the SNMPv1 authorization configuration for devices in the HP Integrated Communication Facility product line.')
icfSecurPassword = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfSecurPassword.setStatus('deprecated')
if mibBuilder.loadTexts: icfSecurPassword.setDescription("********* THIS OBJECT IS DEPRECATED ********* This variable contains a string which is used both as the community name for the password community, and as the login password for the console port. This community name is needed for most SET operations. In addition, the variables in the ICF security group are only visible within the password community, and must use the value of this variable as the community name for GET operations. If the value of this variable is equal to the null string, the community name 'public' or the null string will be treated the same as the password community. This object has been deprecated. Its functionality has been replaced by the icfCommunityTable.")
icfSecurAuthAnyMgr = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfSecurAuthAnyMgr.setStatus('deprecated')
if mibBuilder.loadTexts: icfSecurAuthAnyMgr.setDescription('********* THIS OBJECT IS DEPRECATED ********* When this variable is set to enabled, any manager with a valid community name may perform SET operations on this device. In this configuration, entries in the icfSecurAuthMgrTable are used only for trap destinations. If this variable is set to disabled, a manager must be in the icfSecurAuthMgrTable and have a valid community name in order to perform SET operations. This object has been deprecated. Its functionality has been replaced by the icfAuthMgrTable.')
icfSecurAuthMgrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3), )
if mibBuilder.loadTexts: icfSecurAuthMgrTable.setStatus('deprecated')
if mibBuilder.loadTexts: icfSecurAuthMgrTable.setDescription('********* THIS OBJECT IS DEPRECATED ********* This table contains a list of addresses of managers that are allowed to perform SET operations on this device, and controls the destination addresses for traps. If icfSecurAuthAnyMgr is set to disabled, a manager must be in this table and use the correct community name for the password community in order to perform a GET operation on this table. This table has been deprecated. It is replaced by the icfAuthMgrTable. The trap destination functionality has been replaced by the hpicfTrapDestTable.')
icfSecurAuthMgrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1), ).setIndexNames((0, "HP-ICF-SECURITY", "icfAuthMgrIndex"))
if mibBuilder.loadTexts: icfSecurAuthMgrEntry.setStatus('deprecated')
if mibBuilder.loadTexts: icfSecurAuthMgrEntry.setDescription('********* THIS OBJECT IS DEPRECATED ********* An entry in the icfSecurAuthMgrTable containing information about a single manager. This table has been deprecated. It is replaced by the icfAuthMgrTable. The trap destination functionality has been replaced by the hpicfTrapDestTable.')
icfAuthMgrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfAuthMgrIndex.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthMgrIndex.setDescription('********* THIS OBJECT IS DEPRECATED ********* This object contains the index which uniquely identifies this entry in the icfSecurAuthMgrTable. This table has been deprecated. It is replaced by the icfAuthMgrTable. The trap destination functionality has been replaced by the hpicfTrapDestTable.')
icfAuthMgrIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfAuthMgrIpAddress.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthMgrIpAddress.setDescription('********* THIS OBJECT IS DEPRECATED ********* The IP address of a manager that is allowed to manage this device. Setting this variable to a nonzero value will clear the corresponding instance of the icfAuthMgrIpxAddress variable. This table has been deprecated. It is replaced by the icfAuthMgrTable. The trap destination functionality has been replaced by the hpicfTrapDestTable.')
icfAuthMgrIpxAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfAuthMgrIpxAddress.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthMgrIpxAddress.setDescription('********* THIS OBJECT IS DEPRECATED ********* The IPX address of a manager that is allowed to manage this device. Setting this variable to a valid IPX address will clear the corresponding instance of the icfAuthMgrIpAddress variable. This table has been deprecated. It is replaced by the icfAuthMgrTable. The trap destination functionality has been replaced by the hpicfTrapDestTable.')
icfAuthMgrRcvTraps = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfAuthMgrRcvTraps.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthMgrRcvTraps.setDescription('********* THIS OBJECT IS DEPRECATED ********* If this variable is set to enabled, any traps generated by this device will be sent to the manager indicated by the corresponding instance of either icfAuthMgrIpAddress or icfAuthMgrIpxAddress, whichever is valid. This table has been deprecated. It is replaced by the icfAuthMgrTable. The trap destination functionality has been replaced by the hpicfTrapDestTable.')
icfSecurIntruder = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4))
icfSecurIntruderFlag = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfSecurIntruderFlag.setStatus('current')
if mibBuilder.loadTexts: icfSecurIntruderFlag.setDescription("If this object is set to 'valid', the remainder of the intruder objects contain information about an authentication failure. The Security LED on the device will blink if this flag is set to 'valid'. The intruder objects will not be overwritten as long as this flag is set to 'valid'. Setting this flag to 'invalid' will turn off the Security LED if there are no other current violations, and will allow the intruder objects to be overwritten by subsequent authentication failures.")
icfSecurIntruderIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfSecurIntruderIpAddress.setStatus('current')
if mibBuilder.loadTexts: icfSecurIntruderIpAddress.setDescription('The IP address of the manager that caused the authentication failure. Only one of icfSecurIntruderIpAddress and icfSecurIntruderIPXAddress will be valid.')
icfSecurIntruderIpxAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfSecurIntruderIpxAddress.setStatus('current')
if mibBuilder.loadTexts: icfSecurIntruderIpxAddress.setDescription('The IPX address of the manager that caused the authentication failure. Only one of icfSecurIntruderIpAddress and icfSecurIntruderIPXAddress will be valid.')
icfSecurIntruderTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfSecurIntruderTime.setStatus('current')
if mibBuilder.loadTexts: icfSecurIntruderTime.setDescription('The value of sysUpTime when the authentication failure occurred. A value of 0 indicates that the agent has been reset since this authentication failure occurred.')
icfCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5), )
if mibBuilder.loadTexts: icfCommunityTable.setStatus('deprecated')
if mibBuilder.loadTexts: icfCommunityTable.setDescription('******************DEPRECATED******************* This table contains information about community names known by this agent.')
icfCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1), ).setIndexNames((0, "HP-ICF-SECURITY", "icfCommunityIndex"))
if mibBuilder.loadTexts: icfCommunityEntry.setStatus('deprecated')
if mibBuilder.loadTexts: icfCommunityEntry.setDescription('******************DEPRECATED******************* An entry in the table, containing information about a single community name.')
icfCommunityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: icfCommunityIndex.setStatus('deprecated')
if mibBuilder.loadTexts: icfCommunityIndex.setDescription('******************DEPRECATED******************* Uniquely identifies this community name entry.')
icfCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfCommunityName.setStatus('deprecated')
if mibBuilder.loadTexts: icfCommunityName.setDescription('******************DEPRECATED******************* Community name this entry is about. Not allowed to have two active rows with the same community name.')
icfCommunityReadView = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("discovery", 2), ("restricted", 3), ("user", 4), ("root", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfCommunityReadView.setStatus('deprecated')
if mibBuilder.loadTexts: icfCommunityReadView.setDescription("******************DEPRECATED******************* The MIB view used for read requests using this community name. One of the following: 'none' is the empty MIB view. 'discovery' has access to discovery objects, which will be enough to do an address search, send announce packets, and do a link test. This view also includes objects under the samplingProbe subtree. This view is typically used as a writeView for a community used by autodiscovery and autotopology applications. 'restricted' has access to a limited subset of the MIB, which includes monitoring objects and limited set of configuration objects. 'user' has access to everything except objects under the icfSecurity subtree. 'root' has access to everything, including the icfSecurity subtree.")
icfCommunityWriteView = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("discovery", 2), ("restricted", 3), ("user", 4), ("root", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfCommunityWriteView.setStatus('deprecated')
if mibBuilder.loadTexts: icfCommunityWriteView.setDescription("******************DEPRECATED******************* The MIB view used for write requests using this community name. One of the following: 'none' is the empty MIB view. 'discovery' has access to discovery objects, which will be enough to do an address search, send announce packets, and do a link test. This view also includes objects under the samplingProbe subtree. This view is typically used as a writeView for a community used by autodiscovery and autotopology applications. 'restricted' has access to a limited subset of the MIB, which includes monitoring objects and limited set of configuration objects. 'user' has access to everything except objects under the icfSecurity subtree. 'root' has access to everything, including the icfSecurity subtree.")
icfCommunityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfCommunityStatus.setStatus('deprecated')
if mibBuilder.loadTexts: icfCommunityStatus.setDescription('******************DEPRECATED******************* Status of this entry.')
icfAuthMgrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6), )
if mibBuilder.loadTexts: icfAuthMgrTable.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthMgrTable.setDescription('******************DEPRECATED******************* This table contains a list of manager addresses. Entries in this table are grouped by using a common value for icfCommunityIndex, that identifies the community name that the group of manager addresses has access to. A community name entry which has a set of entries in this table can only be used by requests originating from one of the addresses in the set. A community name entry which has no entries in this table can be used by requests originating from any address.')
icfAuthMgrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1), ).setIndexNames((0, "HP-ICF-SECURITY", "icfCommunityIndex"), (0, "HP-ICF-SECURITY", "icfAuthMgrSubIndex"))
if mibBuilder.loadTexts: icfAuthMgrEntry.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthMgrEntry.setDescription('******************DEPRECATED******************* An entry in the table, containing a single authorized manager address.')
icfAuthMgrSubIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: icfAuthMgrSubIndex.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthMgrSubIndex.setDescription('******************DEPRECATED******************* An index which uniquely identifies an address within a group.')
icfAuthMgrAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ip", 1), ("ipx", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthMgrAddrType.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthMgrAddrType.setDescription('******************DEPRECATED******************* The network type for this entry.')
icfAuthMgrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1, 3), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(10, 10), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthMgrAddress.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthMgrAddress.setDescription("******************DEPRECATED******************* The manager address for this entry, formatted according to the value of icfAuthMgrAddrType. When icfAuthMgrAddrType is 'ip', this value will consist of four octets, containing the IP address of the manager in network byte order. When icfAuthMgrAddrType is 'ipx', this value will consist of ten octets. The first four octets will contain the IPX network number in network byte order, and the remaining six octets will contain the IPX node number in network byte order.")
icfAuthMgrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1, 4), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(10, 10), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthMgrMask.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthMgrMask.setDescription("******************DEPRECATED******************* This object is used to qualify the value of the corresponding instance of icfAuthMgrAddress. The semantics of this object depend on the corresponding value of icfAuthMgrAddrType. When icfAuthMgrType is 'ip', this object can be used to allow access by all managers on a particular IP subnet. When icfAuthMgrType is 'ipx', this object can be used to allow access by all managers with a particular IPX network number.")
icfAuthMgrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthMgrStatus.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthMgrStatus.setDescription('******************DEPRECATED******************* Status of this entry.')
icfAuthIPMgrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7), )
if mibBuilder.loadTexts: icfAuthIPMgrTable.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrTable.setDescription('This table contains a list of IP manager addresses. This list is used grant or deny access to HTTP, telnet, and TFTP.')
icfAuthIPMgrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1), ).setIndexNames((0, "HP-ICF-SECURITY", "icfAuthIPMgrIndex"))
if mibBuilder.loadTexts: icfAuthIPMgrEntry.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrEntry.setDescription('An entry in the table containing a single IP authorized manager address.')
icfAuthIPMgrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: icfAuthIPMgrIndex.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrIndex.setDescription('An index which uniquely identifies an address within the group.')
icfAuthIPMgrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthIPMgrAddress.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthIPMgrAddress.setDescription('**************deprecated********************* The IP address of the authorized manager for this entry. This object is deprecated new object icfAuthIPMgr InetAddress has been defined to hold version neutral address type.')
icfAuthIPMgrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthIPMgrMask.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthIPMgrMask.setDescription('**************deprecated********************** This object qualifies the value of the corresponding instance of icfAuthIPMgrAddress. This object can be used to allow access by all managers on a particular IP subnet. This object is deprecated the new objects which are defined to hold this is value are icfAuthIPMgrInetAddrMaskType and icfAuthIPMgrInetAddrMask.')
icfAuthIPMgrAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("operator", 1), ("manager", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthIPMgrAccess.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrAccess.setDescription('This object defines the access level for a given manager. Operator allows for read only access, and Manager allows for read/write access.')
icfAuthIPMgrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthIPMgrStatus.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrStatus.setDescription('Status of this entry.')
icfAuthIPMgrInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 6), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthIPMgrInetAddrType.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrInetAddrType.setDescription('Specifies the type of address stored in icfAuthIPMgrInetAddress object.')
icfAuthIPMgrInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthIPMgrInetAddress.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrInetAddress.setDescription('The IP address of the authorized manager for this entry.This object can hold the version neutral IP address.')
icfAuthIPMgrInetAddrMaskType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 8), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthIPMgrInetAddrMaskType.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrInetAddrMaskType.setDescription('Specifies the type of IP Mask stored in icfAuthIPMgrInetAddrMask object.')
icfAuthIPMgrInetAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 9), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthIPMgrInetAddrMask.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrInetAddrMask.setDescription('This object qualifies the value of the corresponding instance of icfAuthIPMgrInetAddress. This object can be used to allow access by all managers on a particular IP subnet.This object can hold the version neutral IP address Mask.')
icfAuthIPMgrAccessMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 7, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("all", 1), ("ssh", 2), ("telnet", 3), ("web", 4), ("snmp", 5), ("tftp", 6))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: icfAuthIPMgrAccessMethod.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrAccessMethod.setDescription('This object defines the access method for a given manager. The different access methods are all, ssh, telnet, web, snmp, tftp')
icfSecurityConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1))
icfSecurityCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 1))
icfSecurityGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2))
icfSecurCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 1, 1)).setObjects(("HP-ICF-SECURITY", "icfSnmpSecurityGroup"), ("HP-ICF-SECURITY", "icfSecIntruderGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfSecurCompliance = icfSecurCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: icfSecurCompliance.setDescription('********* THIS COMPLIANCE IS DEPRECATED *********/ A compliance statement for agents implementing the original version of this module.')
icfV1CommunityCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 1, 2)).setObjects(("HP-ICF-SECURITY", "icfV1CommunityGroup"), ("HP-ICF-SECURITY", "icfSecIntruderGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfV1CommunityCompliance = icfV1CommunityCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: icfV1CommunityCompliance.setDescription('********* THIS GROUP IS DEPRECATED ********* A compliance statement for HP ICF agents implementing SNMPv1 community name management.')
icfAuthIPMgrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 1, 3)).setObjects(("HP-ICF-SECURITY", "icfAuthIPMgrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfAuthIPMgrCompliance = icfAuthIPMgrCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthIPMgrCompliance.setDescription('A compliance statement for granting or denying access to specific IP addresses for HTTP, telnet, and TFTP.')
icfAuthIPMgrCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 1, 4)).setObjects(("HP-ICF-SECURITY", "icfAuthIPMgrInetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfAuthIPMgrCompliance1 = icfAuthIPMgrCompliance1.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrCompliance1.setDescription('A compliance statement for granting or denying access to specific IP addresses for HTTP, telnet, and TFTP.')
icfSnmpSecurityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2, 1)).setObjects(("HP-ICF-SECURITY", "icfSecurPassword"), ("HP-ICF-SECURITY", "icfSecurAuthAnyMgr"), ("HP-ICF-SECURITY", "icfAuthMgrIndex"), ("HP-ICF-SECURITY", "icfAuthMgrIpAddress"), ("HP-ICF-SECURITY", "icfAuthMgrIpxAddress"), ("HP-ICF-SECURITY", "icfAuthMgrRcvTraps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfSnmpSecurityGroup = icfSnmpSecurityGroup.setStatus('obsolete')
if mibBuilder.loadTexts: icfSnmpSecurityGroup.setDescription('********* THIS GROUP IS DEPRECATED ********* A collection of objects for managing the SNMPv1 (non-)security configuration on HP networking devices.')
icfSecIntruderGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2, 2)).setObjects(("HP-ICF-SECURITY", "icfSecurIntruderFlag"), ("HP-ICF-SECURITY", "icfSecurIntruderIpAddress"), ("HP-ICF-SECURITY", "icfSecurIntruderIpxAddress"), ("HP-ICF-SECURITY", "icfSecurIntruderTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfSecIntruderGroup = icfSecIntruderGroup.setStatus('current')
if mibBuilder.loadTexts: icfSecIntruderGroup.setDescription('A collection of objects for tracking authentication failures.')
icfV1CommunityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2, 13)).setObjects(("HP-ICF-SECURITY", "icfCommunityName"), ("HP-ICF-SECURITY", "icfCommunityReadView"), ("HP-ICF-SECURITY", "icfCommunityWriteView"), ("HP-ICF-SECURITY", "icfCommunityStatus"), ("HP-ICF-SECURITY", "icfAuthMgrAddrType"), ("HP-ICF-SECURITY", "icfAuthMgrAddress"), ("HP-ICF-SECURITY", "icfAuthMgrMask"), ("HP-ICF-SECURITY", "icfAuthMgrStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfV1CommunityGroup = icfV1CommunityGroup.setStatus('deprecated')
if mibBuilder.loadTexts: icfV1CommunityGroup.setDescription('********* THIS GROUP IS DEPRECATED ********* A collection of objects for managing SNMPv1 community strings.')
icfAuthIPMgrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2, 14)).setObjects(("HP-ICF-SECURITY", "icfAuthIPMgrAddress"), ("HP-ICF-SECURITY", "icfAuthIPMgrMask"), ("HP-ICF-SECURITY", "icfAuthIPMgrAccess"), ("HP-ICF-SECURITY", "icfAuthIPMgrStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfAuthIPMgrGroup = icfAuthIPMgrGroup.setStatus('deprecated')
if mibBuilder.loadTexts: icfAuthIPMgrGroup.setDescription('***************** deprecated ****************** A collection of objects for granting or denying access to specific IP addresses for HTTP, telnet, and TFTP. This Group object has been deprecated and a new group object has been defined with name icfAuthIPMgrInetGroup.')
icfAuthIPMgrInetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1, 1, 2, 15)).setObjects(("HP-ICF-SECURITY", "icfAuthIPMgrInetAddrType"), ("HP-ICF-SECURITY", "icfAuthIPMgrInetAddress"), ("HP-ICF-SECURITY", "icfAuthIPMgrInetAddrMaskType"), ("HP-ICF-SECURITY", "icfAuthIPMgrInetAddrMask"), ("HP-ICF-SECURITY", "icfAuthIPMgrAccessMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfAuthIPMgrInetGroup = icfAuthIPMgrInetGroup.setStatus('current')
if mibBuilder.loadTexts: icfAuthIPMgrInetGroup.setDescription('A collection of objects for granting or denying access to specific IP addresses for HTTP, telnet, and TFTP.')
mibBuilder.exportSymbols("HP-ICF-SECURITY", icfAuthMgrStatus=icfAuthMgrStatus, icfAuthMgrAddrType=icfAuthMgrAddrType, icfCommunityName=icfCommunityName, icfCommunityTable=icfCommunityTable, icfAuthIPMgrStatus=icfAuthIPMgrStatus, icfSecurAuthAnyMgr=icfSecurAuthAnyMgr, icfAuthMgrIpAddress=icfAuthMgrIpAddress, icfSecurAuthMgrTable=icfSecurAuthMgrTable, icfAuthIPMgrInetAddrMask=icfAuthIPMgrInetAddrMask, icfAuthMgrTable=icfAuthMgrTable, icfAuthMgrEntry=icfAuthMgrEntry, icfSecurIntruderIpxAddress=icfSecurIntruderIpxAddress, icfAuthMgrIpxAddress=icfAuthMgrIpxAddress, icfAuthMgrRcvTraps=icfAuthMgrRcvTraps, icfAuthMgrMask=icfAuthMgrMask, icfSecurCompliance=icfSecurCompliance, icfAuthIPMgrAccess=icfAuthIPMgrAccess, icfAuthIPMgrInetAddress=icfAuthIPMgrInetAddress, icfSecurIntruder=icfSecurIntruder, icfAuthIPMgrEntry=icfAuthIPMgrEntry, icfAuthIPMgrAccessMethod=icfAuthIPMgrAccessMethod, icfSecurPassword=icfSecurPassword, icfCommunityReadView=icfCommunityReadView, icfAuthIPMgrMask=icfAuthIPMgrMask, icfCommunityWriteView=icfCommunityWriteView, icfSecurAuthMgrEntry=icfSecurAuthMgrEntry, icfAuthIPMgrAddress=icfAuthIPMgrAddress, icfSecurityGroups=icfSecurityGroups, icfSecIntruderGroup=icfSecIntruderGroup, icfCommunityEntry=icfCommunityEntry, PYSNMP_MODULE_ID=icfSecurityMib, icfAuthIPMgrInetAddrType=icfAuthIPMgrInetAddrType, icfSnmpSecurityGroup=icfSnmpSecurityGroup, icfAuthMgrIndex=icfAuthMgrIndex, icfAuthIPMgrTable=icfAuthIPMgrTable, icfCommunityIndex=icfCommunityIndex, icfSecurityMib=icfSecurityMib, icfV1CommunityGroup=icfV1CommunityGroup, icfAuthIPMgrInetAddrMaskType=icfAuthIPMgrInetAddrMaskType, icfAuthIPMgrCompliance1=icfAuthIPMgrCompliance1, icfAuthIPMgrIndex=icfAuthIPMgrIndex, icfAuthIPMgrInetGroup=icfAuthIPMgrInetGroup, icfSecurIntruderIpAddress=icfSecurIntruderIpAddress, icfSecurityCompliances=icfSecurityCompliances, icfSecurityConformance=icfSecurityConformance, icfSecurIntruderTime=icfSecurIntruderTime, icfAuthIPMgrGroup=icfAuthIPMgrGroup, icfCommunityStatus=icfCommunityStatus, icfSecurIntruderFlag=icfSecurIntruderFlag, icfV1CommunityCompliance=icfV1CommunityCompliance, icfAuthMgrAddress=icfAuthMgrAddress, icfAuthMgrSubIndex=icfAuthMgrSubIndex, icfAuthIPMgrCompliance=icfAuthIPMgrCompliance)
