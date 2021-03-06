#
# PySNMP MIB module CAJUN-POLICY-CAPABILITIES (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CAJUN-POLICY-CAPABILITIES
# Produced by pysmi-0.3.4 at Wed May  1 11:46:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, NotificationType, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, ObjectIdentity, IpAddress, Counter64, MibIdentifier, iso, TimeTicks, enterprises, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "ObjectIdentity", "IpAddress", "Counter64", "MibIdentifier", "iso", "TimeTicks", "enterprises", "ModuleIdentity")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
lucent = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751))
if mibBuilder.loadTexts: lucent.setLastUpdated('0106050000Z')
if mibBuilder.loadTexts: lucent.setOrganization("Avaya's Concord Technology Center (CTC)")
if mibBuilder.loadTexts: lucent.setContactInfo('Shada Al-nasser -- alnasser@avaya.com, Julie Flannery -- jflannery@avaya.com, Virginia Brown -- vibrown@avaya.com')
if mibBuilder.loadTexts: lucent.setDescription('The MIB module for Lucent Policy Enabled CajunRules Products.')
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2))
cajunRulesMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42))
policyCapabilityMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1))
lucentDevicePolicyCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1))
lucentDevicePolicyLDAPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2))
lucentDevicePolicyCapabilityMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 11))
lucentDevicePolicyCapabilityMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 12))
lucentDevicePolicyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 13))
lucentPolicyCapabilityEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 21))
lucentDevicePolicyCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1), )
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityTable.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityTable.setDescription('This table is used to advertise the Policy Capabilities of the Device.')
lucentDevicePolicyCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1), ).setIndexNames((0, "CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityIndex"))
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityEntry.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityEntry.setDescription('Information Describing a single Policy Capability of this device.')
lucentDevicePolicyCapabilityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityIndex.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityIndex.setDescription('A unique index for this entry with no semanitics aside from its uniqueness.')
lucentDevicePolicyCapabilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("ldap", 1), ("cops", 2), ("diameter", 3), ("snmp", 4), ("radius", 5), ("cli", 6), ("other", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityType.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityType.setDescription("An enumeration describing a type of Policy attribute supported by this device. This Policy attribute's semantics is intended to make sense within the context of the CajunRules application. At this time, a value of 'ldap' indicates that the device is retrieving policy information from an LDAP server. This implies that the device also implements the LDAP Group defined in this MIB. At this time the other enumerations are informational only and are intended for future enhancements. It should be noted that 'snmp' indicates that the policies themselves are being set by SNMP. The implementation of the producer/consumer handshake defined in this MIB in the LDAP group does NOT require the lucentDevicePolicyCapabilityType to be set to 'snmp'. The value 'cli' is intended for a proprietary implementation of cli functionality implemented over some proprietary port. This value does NOT refer to the device's implementation of a local command line interface or a command line interface supported over a telnet interface.")
lucentDevicePolicyCapabilityDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityDescription.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityDescription.setDescription('An Infomational string that should be able to be displayed as an identifier for a user. A recommended format would be the type followed by version information if applicable and anything else deemed useful.')
lucentDevicePolicyCapabilityInformation = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityInformation.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityInformation.setDescription('An opaque string to allow for future capabilities.')
lucentDevicePolicyCapabilityState = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityState.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityState.setDescription('The state of this Policy Capability. An inactive state implies that the device has the capacity but is not using it currently.')
lucentDevicePolicyCapabilityRetrievalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("failedRetrieval", 2), ("failedExecution", 3), ("inProgress", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityRetrievalStatus.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityRetrievalStatus.setDescription("Device Retrieval Status from the LDAP Server: success - Retrieval from the LDAP server succeeded and was executed. failedRetrieval - Failure retrieving the policy from the LDAP server. failedExecution - Failure executing the retrieved policy. inProgress - Retrieval from the LDAP server is still in progress. The management station should poll the device until one of the definitive values (success or failed) is returned. For a status of failed-execution, examine the switch's log file to see the exact errors.")
lucentDevicePolicyCapabilityExecutionOption = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stopOnError", 1), ("ignoreErrors", 2))).clone('stopOnError')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityExecutionOption.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityExecutionOption.setDescription('Execution Option for the policy retrieved from the LDAP Server: stopOnError - Execution stops on the first error. ignoreErrors - Execution continues in spite of errors; the commands with errors are ignored.')
lucentDevicePolicyTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyTime.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyTime.setDescription('The base time that the device would like policies to be based upon. This field is primarily intended to allow the device to advertise its time zone. If this time zone is not present, or if this object is not implemented, the client device willuse it local time zone. Syncronization of time information other than the time zone is best-effort.')
lucentDevicePolicyCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 13, 1)).setObjects(("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityIndex"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityType"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityDescription"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityInformation"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityState"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lucentDevicePolicyCapabilityGroup = lucentDevicePolicyCapabilityGroup.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityGroup.setDescription('A group defining the minimum implementation of a device instrumenting the Device Policy Capabilities MIB.')
lucentDevicePolicyLDAPServerIP = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicyLDAPServerIP.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyLDAPServerIP.setDescription("The IP address of the LDAP enabled server this device retreives policy information from. By convention, setting this value to 0 disables the directory enabled capablity of this device with respect to policy. If the devices's directory enabled capability with respect to policy is disabled locally, this object will be clearedd.")
lucentDevicePolicyLDAPServerPort = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicyLDAPServerPort.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyLDAPServerPort.setDescription('The well-known port over which this device is using LDAP. It is assumed that ports other than 389 might be utilized.')
lucentDevicePolicySecondaryLDAPServerIP = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicySecondaryLDAPServerIP.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicySecondaryLDAPServerIP.setDescription('The backup LDAP server IP Address.')
lucentDevicePolicySecondaryLDAPServerPort = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicySecondaryLDAPServerPort.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicySecondaryLDAPServerPort.setDescription('The backup LDAP port.')
lucentDevicePolicyBadLDAPObject = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyBadLDAPObject.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyBadLDAPObject.setDescription("The last LDAP Object that was unable to be processed, thereby causing the sending of a lucentBadLDAPObject Notification. If this condition has never ocurred since agent initialization, or if the device cannot 'remember', it would be NULL. The primary purpose of this object is to be included in the lucentBadLDAPObject Notification.")
lucentDevicePolicyBadLDAPDescription = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyBadLDAPDescription.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyBadLDAPDescription.setDescription("A Descriptive string intended to provide optional detail accompanying a lucentDadLDAPObject Notification. A likely use of this string would be for the receiver of this variable in a trap to display the string in an error log. If this condition has never ocurred since agent initialization, or if the device cannot 'remember',it would be NULL. The primary purpose of this object is to be included in the lucentBadLDAPObject Notification.")
lucentDevicePolicyCapabilityLastChange = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityLastChange.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityLastChange.setDescription("The sysUpTime in the device that this Policy Capability was last modified. Providing this allows a remote manager to detect a change in the Policy Capabilities by polling a single object. On seeing this value change an interested manager should relearn this device's Policy Capabilities.")
lucentDevicePolicyCapabilityProducerSignal = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityProducerSignal.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityProducerSignal.setDescription("The sequence number assocated with the latest policy written for this device at the directory 'pointed to' by lucentDevicePolicyLDAPServerIP. This sequence number is part of the Directory's Policy schema. This object is designed for writing to by a CajunRules like manager when it has placed a new policy for retrieval and can be interpreted by the device as a signal to retrieve this policy. By convention, this device would never be written to by the agent with the exception of it being cleared at system initializaton time. In tandem with the lucentDevicePolicyCapabilityConsumerSignal it should describe the current state of the device with respect to its LDAP Policy retrieval behavior.")
lucentDevicePolicyCapabilityConsumerSignal = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityConsumerSignal.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityConsumerSignal.setDescription("The sequence number of the last Policy retrieved from the directory 'pointed to' by lucentDevicePolicyLDAPServerIP. This sequence number is part of the Directory Policy schema. This object is initialized at zero on agent reset, and thereafter only written by the Policy Agent on successful retrieval and parsing of a Policy Schema from the directory. In tandem with the lucentDevicePolicyCapabilityConsumerSignal it should describe the current state of the device with respect to its LDAP Policy retrieval behavior. By convention, the agent may set this value to 0xffff to indicate an error serious enough to prohibit its enforcing a retrieved policy.")
lucentDevicePolicyLDAPSearchBase = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 2, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lucentDevicePolicyLDAPSearchBase.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyLDAPSearchBase.setDescription('The search base string to be used by the LDAP client.')
lucentDevicePolicyCapabilityLDAPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 13, 2)).setObjects(("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerIP"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerPort"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicySecondaryLDAPServerIP"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicySecondaryLDAPServerPort"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPObject"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPDescription"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityLastChange"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityProducerSignal"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityConsumerSignal"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPSearchBase"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lucentDevicePolicyCapabilityLDAPGroup = lucentDevicePolicyCapabilityLDAPGroup.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityLDAPGroup.setDescription('A group of the Device Policy Capabilities MIB that defines LDAP specific objects. This group is intended to be implemented by any device that implements an LDAP client to retrieve policy information.')
lucentPolicyCapabilityEventsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 21, 1))
if mibBuilder.loadTexts: lucentPolicyCapabilityEventsV2.setStatus('current')
if mibBuilder.loadTexts: lucentPolicyCapabilityEventsV2.setDescription('The events related to Policy Capabilities.')
lucentBadLDAPObject = NotificationType((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 21, 1, 1)).setObjects(("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerIP"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyLDAPServerPort"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPObject"), ("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyBadLDAPDescription"))
if mibBuilder.loadTexts: lucentBadLDAPObject.setStatus('current')
if mibBuilder.loadTexts: lucentBadLDAPObject.setDescription('A lucentBadLDAPObject trap indicates that the sender has retrieved an LDAP object that it could not process. More details can be copied to lucentDevicePolicyBadLDAPDescription DisplayString.')
lucentDevicePolicyCapabilityBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1751, 2, 42, 1, 12, 1)).setObjects(("CAJUN-POLICY-CAPABILITIES", "lucentDevicePolicyCapabilityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lucentDevicePolicyCapabilityBasicCompliance = lucentDevicePolicyCapabilityBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: lucentDevicePolicyCapabilityBasicCompliance.setDescription('The basic implementation requirements of a policy enabled device.')
mibBuilder.exportSymbols("CAJUN-POLICY-CAPABILITIES", PYSNMP_MODULE_ID=lucent, lucentDevicePolicyCapabilityInformation=lucentDevicePolicyCapabilityInformation, lucentDevicePolicyCapabilityIndex=lucentDevicePolicyCapabilityIndex, cajunRulesMIB=cajunRulesMIB, lucentDevicePolicyCapabilityProducerSignal=lucentDevicePolicyCapabilityProducerSignal, lucentBadLDAPObject=lucentBadLDAPObject, lucent=lucent, lucentDevicePolicyLDAPServerPort=lucentDevicePolicyLDAPServerPort, lucentDevicePolicyCapabilityEntry=lucentDevicePolicyCapabilityEntry, lucentDevicePolicyLDAPObjects=lucentDevicePolicyLDAPObjects, lucentDevicePolicyCapabilityState=lucentDevicePolicyCapabilityState, policyCapabilityMIB=policyCapabilityMIB, lucentPolicyCapabilityEvents=lucentPolicyCapabilityEvents, lucentDevicePolicyBadLDAPObject=lucentDevicePolicyBadLDAPObject, lucentDevicePolicyBadLDAPDescription=lucentDevicePolicyBadLDAPDescription, lucentDevicePolicyMIBGroups=lucentDevicePolicyMIBGroups, lucentDevicePolicyCapabilityLDAPGroup=lucentDevicePolicyCapabilityLDAPGroup, lucentDevicePolicyLDAPSearchBase=lucentDevicePolicyLDAPSearchBase, lucentDevicePolicyCapabilityDescription=lucentDevicePolicyCapabilityDescription, lucentDevicePolicyCapabilityMIBCompliances=lucentDevicePolicyCapabilityMIBCompliances, lucentDevicePolicyCapabilities=lucentDevicePolicyCapabilities, mibs=mibs, lucentDevicePolicyCapabilityRetrievalStatus=lucentDevicePolicyCapabilityRetrievalStatus, lucentDevicePolicyCapabilityExecutionOption=lucentDevicePolicyCapabilityExecutionOption, lucentDevicePolicyCapabilityBasicCompliance=lucentDevicePolicyCapabilityBasicCompliance, lucentDevicePolicyCapabilityTable=lucentDevicePolicyCapabilityTable, lucentDevicePolicyTime=lucentDevicePolicyTime, lucentDevicePolicyLDAPServerIP=lucentDevicePolicyLDAPServerIP, lucentPolicyCapabilityEventsV2=lucentPolicyCapabilityEventsV2, lucentDevicePolicyCapabilityConsumerSignal=lucentDevicePolicyCapabilityConsumerSignal, lucentDevicePolicyCapabilityType=lucentDevicePolicyCapabilityType, lucentDevicePolicyCapabilityMIBConformance=lucentDevicePolicyCapabilityMIBConformance, lucentDevicePolicySecondaryLDAPServerIP=lucentDevicePolicySecondaryLDAPServerIP, lucentDevicePolicyCapabilityLastChange=lucentDevicePolicyCapabilityLastChange, lucentDevicePolicyCapabilityGroup=lucentDevicePolicyCapabilityGroup, lucentDevicePolicySecondaryLDAPServerPort=lucentDevicePolicySecondaryLDAPServerPort)
