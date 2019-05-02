#
# PySNMP MIB module ERI-DNX-STS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERI-DNX-STS1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:06:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
FunctionSwitch, DecisionType, LinkPortAddress, trapSequence, PortStatus, LinkCmdStatus, devices = mibBuilder.importSymbols("ERI-DNX-SMC-MIB", "FunctionSwitch", "DecisionType", "LinkPortAddress", "trapSequence", "PortStatus", "LinkCmdStatus", "devices")
eriMibs, = mibBuilder.importSymbols("ERI-ROOT-SMI", "eriMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ObjectIdentity, iso, Unsigned32, Gauge32, TimeTicks, IpAddress, Counter32, MibIdentifier, NotificationType, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "iso", "Unsigned32", "Gauge32", "TimeTicks", "IpAddress", "Counter32", "MibIdentifier", "NotificationType", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eriDNXSts1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 644, 3, 4))
if mibBuilder.loadTexts: eriDNXSts1MIB.setLastUpdated('200204080000Z')
if mibBuilder.loadTexts: eriDNXSts1MIB.setOrganization('Eastern Research, Inc.')
if mibBuilder.loadTexts: eriDNXSts1MIB.setContactInfo('Customer Service Postal: Eastern Research, Inc. 225 Executive Drive Moorestown, NJ 08057 Phone: +1-800-337-4374 Email: support@erinc.com')
if mibBuilder.loadTexts: eriDNXSts1MIB.setDescription('The ERI Enterprise MIB Module for the DNX STS1 Device.')
dnxSTS1 = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3))
sts1Config = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1))
sts1Diag = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2))
class VtGroupType(TextualConvention, Integer32):
    description = 'Indicates the type of Virtual Tributaries (VT) grouping option used on the links. VT 1.5 is used to group T1 links into 7 groups of 4 for the 28 links. VT 2.0 is used to group E1 links into 7 groups of 3 for the 21 links. Using the VT 2.0, links divisible by 4 are skipped over and not used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("vt2-0-e1", 0), ("vt1-5-ds1", 1))

sts1MapperConfigTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1), )
if mibBuilder.loadTexts: sts1MapperConfigTable.setStatus('current')
if mibBuilder.loadTexts: sts1MapperConfigTable.setDescription('This is the STS-1 Mapper LIU Configuration table which consists of an entry for each of the STS-1 cards. The total number of entries depends on the number of STS-1 cards in the nest.')
sts1MapperConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1), ).setIndexNames((0, "ERI-DNX-STS1-MIB", "sts1MapperAddr"))
if mibBuilder.loadTexts: sts1MapperConfigEntry.setStatus('current')
if mibBuilder.loadTexts: sts1MapperConfigEntry.setDescription('The conceptual row of the STS-1 Mapper LIU Configuration table. A row in this table cannot be added or deleted, only modified.')
sts1MapperAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperAddr.setStatus('current')
if mibBuilder.loadTexts: sts1MapperAddr.setDescription('This number uniquely identifies a STS-1 slot/mapper.')
sts1MapperResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperResource.setStatus('current')
if mibBuilder.loadTexts: sts1MapperResource.setDescription('Uniquely identifies an STS1 Device in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
sts1VtGroup1 = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 3), VtGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1VtGroup1.setStatus('current')
if mibBuilder.loadTexts: sts1VtGroup1.setDescription('Indicates the type of grouping option used to on links 1 through 4. Using the VT 2.0, link 4 is not used.')
sts1VtGroup2 = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 4), VtGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1VtGroup2.setStatus('current')
if mibBuilder.loadTexts: sts1VtGroup2.setDescription('Indicates the type of grouping option used to on links 5 through 8. Using the VT 2.0, link 8 is not used.')
sts1VtGroup3 = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 5), VtGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1VtGroup3.setStatus('current')
if mibBuilder.loadTexts: sts1VtGroup3.setDescription('Indicates the type of grouping option used to on links 9 through 12. Using the VT 2.0, link 12 is not used.')
sts1VtGroup4 = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 6), VtGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1VtGroup4.setStatus('current')
if mibBuilder.loadTexts: sts1VtGroup4.setDescription('Indicates the type of grouping option used to on links 13 through 16. Using the VT 2.0, link 16 is not used.')
sts1VtGroup5 = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 7), VtGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1VtGroup5.setStatus('current')
if mibBuilder.loadTexts: sts1VtGroup5.setDescription('Indicates the type of grouping option used to on links 17 through 20. Using the VT 2.0, link 20 is not used.')
sts1VtGroup6 = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 8), VtGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1VtGroup6.setStatus('current')
if mibBuilder.loadTexts: sts1VtGroup6.setDescription('Indicates the type of grouping option used to on links 21 through 24. Using the VT 2.0, link 24 is not used.')
sts1VtGroup7 = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 9), VtGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1VtGroup7.setStatus('current')
if mibBuilder.loadTexts: sts1VtGroup7.setDescription('Indicates the type of grouping option used to on links 25 through 28. Using the VT 2.0, link 28 is not used.')
sts1VtMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("standardVT", 0), ("sequencialFrm", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1VtMapping.setStatus('current')
if mibBuilder.loadTexts: sts1VtMapping.setDescription('Indicates the Mapper Standard currently in use.')
sts1Timing = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("internal", 0), ("ec1-Line", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1Timing.setStatus('current')
if mibBuilder.loadTexts: sts1Timing.setDescription('Indicates whether the STS-1 device uses an internal or external clock source.')
sts1ShortCable = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 12), FunctionSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1ShortCable.setStatus('current')
if mibBuilder.loadTexts: sts1ShortCable.setDescription("Indicates the line build out of the STS-1 transmitter. 'enable' when attached to a cable less than 50 feet long.")
sts1MaprCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 1, 1, 13), LinkCmdStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1MaprCmdStatus.setStatus('current')
if mibBuilder.loadTexts: sts1MaprCmdStatus.setDescription('The command status for this link configuration row/record. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. Default Response State used in GET RESPONSE Command ready-for-command (0) initial default status for a row STS1 Link Commands used in SET Command (1..199) update-link-config(1), Change existing Link Configuration Response States used in GET RESPONSE Command (200..399) update-successful (201) Link data has been successfully changed STS1 Mapper Config Error Codes used in GET RESPONSE Command (400..699) err-general-link-config-error (400) Unknown link configuration error occurred err-invalid-link-status (401) Unrecognized link status setting err-invalid-link-framing (402) Line framing type not valid for link type err-invalid-link-command (403) Unrecognized link command-action err-invalid-link-op-mode (407) Configured M13 Op mode not valid for port; verify other link parameters match desired new mode err-invalid-link-rem-loop (408) Remote Loop type not valid for sts1 frame type err-invalid-link-ais (409) Unrecognized sts1 AIS selection err-data-locked-by-another-user (450) Another administrative user is making changes to this part of the system via a terminal session. Check Event Log for user name err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big')
sts1T1E1LinkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2), )
if mibBuilder.loadTexts: sts1T1E1LinkConfigTable.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1LinkConfigTable.setDescription("This is the STS T1/E1 Link Configuration table which consists of an entry for each of the card's 28 links. The total number of entries depends on the number of STS1 cards in the nest.")
sts1T1E1LinkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1), ).setIndexNames((0, "ERI-DNX-STS1-MIB", "sts1T1E1CfgLinkAddr"))
if mibBuilder.loadTexts: sts1T1E1LinkConfigEntry.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1LinkConfigEntry.setDescription('The conceptual row of the STS T1/E1 Link Configuration table. A row in this table cannot be added or deleted, only modified.')
sts1T1E1CfgLinkAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1T1E1CfgLinkAddr.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1CfgLinkAddr.setDescription('This number uniquely identifies a STS T1/E1 link resource. This number will be used throughout the system to identify a unique resource.')
sts1T1E1CfgResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1T1E1CfgResource.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1CfgResource.setDescription('Uniquely identifies an STS T1/E1 Channel in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
sts1T1E1CfgLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1T1E1CfgLinkName.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1CfgLinkName.setDescription('This is the user friendly text name to identify the link.')
sts1T1E1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 4), PortStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1T1E1Status.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1Status.setDescription('Dictates the current status of the link, in-service or out-of-service.')
sts1T1E1Clear = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("framed", 1), ("unframed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1T1E1Clear.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1Clear.setDescription('Determines if the port supports T1 or E1 unframed.')
sts1T1E1Framing = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 6, 7))).clone(namedValues=NamedValues(("t1Esf", 5), ("t1D4", 6), ("t1Unframed", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1T1E1Framing.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1Framing.setDescription("Determines the type of framing used on the line. Choose between T1 SuperFrame 'D4', Extended SuperFrame (ESF), or T1 Unframed. Currently E1 is not supported. When value of sts1T1E1Clear is set to unframed (2), the only valid framing options are: e1Unframed(4) or t1Unframed(7).")
sts1T1E1NetLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 7), FunctionSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1T1E1NetLoop.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1NetLoop.setDescription("Determines whether or not the module should respond to loop diagnostic commands received from the network supplier. Select 'enable' unless the commands are to be passed to another STS1 device.")
sts1T1E1YelAlrm = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 8), DecisionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1T1E1YelAlrm.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1YelAlrm.setDescription("Causes the module to discard data and send a yellow alarm if it is in a red alarm condition after a 3 second period. 'Yes' must be chosen if the network supplier is a common carrier, such as a telephone company.")
sts1T1E1RecoverTime = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 10, 15))).clone(namedValues=NamedValues(("timeout-3-secs", 3), ("timeout-10-secs", 10), ("timeout-15-secs", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1T1E1RecoverTime.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1RecoverTime.setDescription('This is the red alarm timeout value. Determines the amount of seconds the port will wait to stop sending the yellow alarm when coming out of a red alarm condition.')
sts1T1E1EsfFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("att-54016", 0), ("ansi-t1-403", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1T1E1EsfFormat.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1EsfFormat.setDescription('Determines the type of ESF network commands the T-1 link will respond to. It has no meaning for D4 networks. With ESF networks, this information must be obtained from the network supplier.')
sts1T1E1IdleCode = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("busy", 0), ("idle", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1T1E1IdleCode.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1IdleCode.setDescription("Determines the whether the code that will be transmitted over the unused links will be 'idle' or 'busy' (all 1's).")
sts1T1E1CfgCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 12), LinkCmdStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1T1E1CfgCmdStatus.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1CfgCmdStatus.setDescription("The command status for this link configuration row/record. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. Default Response State used in GET RESPONSE Command ready-for-command (0) initial default status for a row STS1-T1 Link Commands used in SET Command (1..199) update(1) Change existing Link Configuration inServiceAll (7) Change Link Status to in-service for all 8 links. copyToAll (9) Copy T1 Link configuration to all other links within the same device outOfServiceAll (12) Change Link Status to out-of-service for all 8 links. Response States used in GET RESPONSE Command (100..199) update-successful (101) Link data has been successfully changed insvc-successful (107) All Links have been successfully placed In Service copy-successful (109) T1 Link data has been successfully copied to other links oos-successful (112) All Links have been successfully placed Out of Service STS1-T1 Link Config Error Codes used in GET RESPONSE Command (400..699) err-general-link-config-error (400) Unknown link configuration error occurred err-invalid-link-status (401) Unrecognized link status setting err-invalid-link-framing (402) Line framing type not valid for link type err-invalid-link-command (403) Unrecognized link command-action err-invalid-esf-format (405) ESF type not applicable to link type err-invalid-link-density (406) Unrecognized T1 link density setting err-invalid-network-loop (410) Unrecognized network loop setting err-invalid-yellow-alrm (411) Unrecognized yellow alarm setting err-invalid-red-timeout (412) Unrecognized red alarm timeout err-invalid-idle-code (413) Unrecognized idle code err-device-in-standby (414) Can't change config for designated Standby device err-data-locked-by-another-user (450) Another administrative user is making changes to this part of the system via a terminal session. Check Event Log for user name err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big")
sts1T1E1Gr303Facility = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 1, 2, 1, 13), DecisionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1T1E1Gr303Facility.setStatus('obsolete')
if mibBuilder.loadTexts: sts1T1E1Gr303Facility.setDescription('Enables link to be configured as a Gr303 Facility')
sts1MapperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1), )
if mibBuilder.loadTexts: sts1MapperStatusTable.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusTable.setDescription("This is the STS-1 Mapper Status table which consists of a single entry for each card's Mapper Display. The total number of entries depends on the number of STS1 cards in the node.")
sts1MapperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1), ).setIndexNames((0, "ERI-DNX-STS1-MIB", "sts1MapperStatusAddr"))
if mibBuilder.loadTexts: sts1MapperStatusEntry.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusEntry.setDescription('The conceptual row of the Mapper table. A row in this table cannot be added or deleted, only modified.')
sts1MapperStatusAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperStatusAddr.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusAddr.setDescription('This number uniquely identifies a STS1 Mapper resource. This number will be used throughout the system to identify a unique resource.')
sts1MapperStatusResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperStatusResource.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusResource.setDescription('This number uniquely identifies a STS1 Mapper resource. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table Entry.')
sts1MapperStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 32, 256, 512, 1024, 8192, 131072, 2147483647))).clone(namedValues=NamedValues(("ok", 0), ("lof", 32), ("lop", 256), ("oof", 512), ("ais", 1024), ("los", 8192), ("lomf", 131072), ("errors", 2147483647)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperStatusState.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusState.setDescription('Determines the current line condition status of the Mapper. ok (0), lof (32), -- bit 5 lop (256), -- bit 8 oof (512), -- bit 9 ais (1024), -- bit 10 los (8192), -- bit 13 lomf (131072), -- bit 17 errors (2147483647) -- all ')
sts1MapperStatusLOSErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperStatusLOSErrs.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusLOSErrs.setDescription('This is the number of seconds a Loss of Signal was declared.')
sts1MapperStatusOOFErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperStatusOOFErrs.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusOOFErrs.setDescription('This is the number of seconds an Out Of Frame alignement error was declared.')
sts1MapperStatusLOFErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperStatusLOFErrs.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusLOFErrs.setDescription('This is the number of seconds a Loss of Frame was declared.')
sts1MapperStatusLOPtrErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperStatusLOPtrErrs.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusLOPtrErrs.setDescription('This is the number of seconds a Loss of Pointer was declared.')
sts1MapperStatusAISErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperStatusAISErrs.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusAISErrs.setDescription('This is the number of seconds an Alarm Indication Signal was declared.')
sts1MapperStatusMultiFErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperStatusMultiFErrs.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusMultiFErrs.setDescription('This is the number of seconds a Near End Loss of Multi-Frame Signal was declared.')
sts1MapperStatusRxTraceErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperStatusRxTraceErrs.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusRxTraceErrs.setDescription('This is the number of seconds an error has been detected in the receive path trace.')
sts1MapperStatusTotErrSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1MapperStatusTotErrSecs.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusTotErrSecs.setDescription('This is the total number of Errored Seconds.')
sts1MapperStatusCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 14, 101, 114, 200, 206, 500, 501, 502))).clone(namedValues=NamedValues(("ready-for-command", 0), ("update", 1), ("clearErrors", 14), ("update-successful", 101), ("clear-successful", 114), ("err-general-test-error", 200), ("err-field-cannot-be-set", 206), ("err-snmp-parse-failed", 500), ("err-invalid-snmp-type", 501), ("err-invalid-snmp-var-size", 502)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1MapperStatusCmdStatus.setStatus('current')
if mibBuilder.loadTexts: sts1MapperStatusCmdStatus.setDescription('This is the command status for the Mapper Row. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. Default Response State used in GET RESPONSE Command ready-for-command (0) initial default status for a row Action Commands used in SET Command (1..99) update (1) Can be used optionally when activating loops and berts in order to get status code back in response clearErrors (14) Resets all error counters to zero Response States used in GET RESPONSE Command (100..199) update-successful (101) Test action has been successfully performed clear-successful (114) Error counts have been successfully cleared The Error Codes used in GET RESPONSE Command (200..799) err-general-test-error (200) Unknown Test request error occurred. err-field-cannot-be-set (206) Read-only field was included in SET request err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big')
sts1LIUTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2), )
if mibBuilder.loadTexts: sts1LIUTable.setStatus('current')
if mibBuilder.loadTexts: sts1LIUTable.setDescription("This is the STS1 LIU Diagnostic Status table which consists of an entry for each STS1 card's Line Interface Unit Display. The number of entries depends on the number of STS1 cards in the node.")
sts1LIUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1), ).setIndexNames((0, "ERI-DNX-STS1-MIB", "sts1LIUAddr"))
if mibBuilder.loadTexts: sts1LIUEntry.setStatus('current')
if mibBuilder.loadTexts: sts1LIUEntry.setDescription('The conceptual row of the Mapper table. A row in this table cannot be added or deleted, only modified.')
sts1LIUAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 1), LinkPortAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1LIUAddr.setStatus('current')
if mibBuilder.loadTexts: sts1LIUAddr.setDescription('This number uniquely identifies a STS1 Mapper resource address. This number will be used throughout the system to identify a unique resource.')
sts1LIUResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1LIUResource.setStatus('current')
if mibBuilder.loadTexts: sts1LIUResource.setDescription('This number uniquely identifies a STS1 Mapper resource. This number is provided as a key to allow the manager to map this entry to a corresponding Resource Table Entry.')
sts1LIUBertState = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(45, 44))).clone(namedValues=NamedValues(("off", 45), ("liu-bert", 44)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1LIUBertState.setStatus('current')
if mibBuilder.loadTexts: sts1LIUBertState.setDescription('This is the LIU Bert State indicated by on/off.')
sts1LIUBertErrSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1LIUBertErrSecs.setStatus('current')
if mibBuilder.loadTexts: sts1LIUBertErrSecs.setDescription('This is the number of LIU Bert Errored seconds.')
sts1LIUBertDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1LIUBertDuration.setStatus('current')
if mibBuilder.loadTexts: sts1LIUBertDuration.setDescription('This is the number of seconds for the LIU Bert Duration.')
sts1LIULoopType = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 39))).clone(namedValues=NamedValues(("off", 0), ("mapper", 1), ("liu", 39)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1LIULoopType.setStatus('current')
if mibBuilder.loadTexts: sts1LIULoopType.setDescription('Indicates the loopback status of the Mapper/LIU for this STS1 device. off (0) - indicates loopback is disabled mapper (1) - indicates Mapper local data is looped back to itself liu (39)- indicates Line Interface Unit local data is looped back to itself.')
sts1LIUDigitalErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1LIUDigitalErrs.setStatus('current')
if mibBuilder.loadTexts: sts1LIUDigitalErrs.setDescription('This is the number of seconds recorded for the LIU Digital Errors.')
sts1LIUAnalogErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1LIUAnalogErrs.setStatus('current')
if mibBuilder.loadTexts: sts1LIUAnalogErrs.setDescription('This is the number of seconds recorded for the LIU Analog Errors.')
sts1LIUExcessZeros = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1LIUExcessZeros.setStatus('current')
if mibBuilder.loadTexts: sts1LIUExcessZeros.setDescription('This is the number of seconds LIU Excess zero errors were detected.')
sts1LIUCodingViolationErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1LIUCodingViolationErrs.setStatus('current')
if mibBuilder.loadTexts: sts1LIUCodingViolationErrs.setDescription('This is the total number of Errored Seconds for the LIU Coding Violation.')
sts1LIUPRBSErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sts1LIUPRBSErrs.setStatus('current')
if mibBuilder.loadTexts: sts1LIUPRBSErrs.setDescription('This is the total number of Errored Seconds for the LIU PRBS check.')
sts1LIUCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 2, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 14, 101, 114, 200, 202, 203, 205, 206, 500, 501, 502))).clone(namedValues=NamedValues(("ready-for-command", 0), ("update", 1), ("clearErrors", 14), ("update-successful", 101), ("clear-successful", 114), ("err-general-test-error", 200), ("err-invalid-loop-type", 202), ("err-invalid-bert-type", 203), ("err-test-in-progress", 205), ("err-field-cannot-be-set", 206), ("err-snmp-parse-failed", 500), ("err-invalid-snmp-type", 501), ("err-invalid-snmp-var-size", 502)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sts1LIUCmdStatus.setStatus('current')
if mibBuilder.loadTexts: sts1LIUCmdStatus.setDescription('This is the command status for the LIU Mapper Row. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. Default Response State used in GET RESPONSE Command ready-for-command (0) initial default status for a row LIU Action Commands used in SET Command (1..99) update (1) Can be used optionally when activating loops and berts in order to get status code back in response clearErrors (14) Resets all error counters and bert test time to zero Response States used in GET RESPONSE Command (100..199) update-successful (101) Test action has been successfully performed clear-successful (114) Error counts have been successfully cleared LIU Test Error Codes used in GET RESPONSE Command (200..799) err-general-test-error (200) Unknown Test request error occurred. err-invalid-loop-type (202) Unrecognized loop selection err-invalid-bert-type (203) Unrecognized bert selection err-test-in-progress (205) Requested action cannot be performed during bert err-field-cannot-be-set (206) Read-only field was included in SET request err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big')
dnxSTS1Enterprise = ObjectIdentity((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 0))
if mibBuilder.loadTexts: dnxSTS1Enterprise.setStatus('current')
if mibBuilder.loadTexts: dnxSTS1Enterprise.setDescription('ERI DNX STS1 Enterprise for Alarms/Events')
sts1MapperConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 0, 1)).setObjects(("ERI-DNX-SMC-MIB", "trapSequence"), ("ERI-DNX-STS1-MIB", "sts1MapperAddr"), ("ERI-DNX-STS1-MIB", "sts1MaprCmdStatus"))
if mibBuilder.loadTexts: sts1MapperConfigTrap.setStatus('current')
if mibBuilder.loadTexts: sts1MapperConfigTrap.setDescription('This trap is used to notify a NMS that a user has updated the Link configuration for a given STS1 Mapper entry.')
sts1T1E1ConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 3, 0, 2)).setObjects(("ERI-DNX-SMC-MIB", "trapSequence"), ("ERI-DNX-STS1-MIB", "sts1T1E1CfgLinkAddr"), ("ERI-DNX-STS1-MIB", "sts1T1E1CfgCmdStatus"))
if mibBuilder.loadTexts: sts1T1E1ConfigTrap.setStatus('current')
if mibBuilder.loadTexts: sts1T1E1ConfigTrap.setDescription('This trap is used to notify a NMS that a user has updated the Link configuration for a given STS-1 T1 channel entry.')
mibBuilder.exportSymbols("ERI-DNX-STS1-MIB", sts1MapperAddr=sts1MapperAddr, sts1T1E1Framing=sts1T1E1Framing, sts1T1E1CfgResource=sts1T1E1CfgResource, sts1VtGroup6=sts1VtGroup6, PYSNMP_MODULE_ID=eriDNXSts1MIB, sts1VtGroup5=sts1VtGroup5, sts1MapperStatusCmdStatus=sts1MapperStatusCmdStatus, sts1LIUResource=sts1LIUResource, sts1LIUCmdStatus=sts1LIUCmdStatus, sts1LIUTable=sts1LIUTable, sts1MapperStatusLOPtrErrs=sts1MapperStatusLOPtrErrs, sts1Timing=sts1Timing, sts1MapperConfigTable=sts1MapperConfigTable, sts1LIUAddr=sts1LIUAddr, sts1Config=sts1Config, sts1T1E1ConfigTrap=sts1T1E1ConfigTrap, sts1LIULoopType=sts1LIULoopType, sts1LIUBertState=sts1LIUBertState, sts1MapperStatusOOFErrs=sts1MapperStatusOOFErrs, eriDNXSts1MIB=eriDNXSts1MIB, sts1MapperStatusTable=sts1MapperStatusTable, sts1T1E1CfgLinkAddr=sts1T1E1CfgLinkAddr, sts1T1E1EsfFormat=sts1T1E1EsfFormat, sts1MapperStatusEntry=sts1MapperStatusEntry, sts1LIUExcessZeros=sts1LIUExcessZeros, sts1LIUPRBSErrs=sts1LIUPRBSErrs, sts1LIUAnalogErrs=sts1LIUAnalogErrs, sts1T1E1CfgLinkName=sts1T1E1CfgLinkName, sts1ShortCable=sts1ShortCable, sts1VtMapping=sts1VtMapping, sts1T1E1YelAlrm=sts1T1E1YelAlrm, sts1T1E1Status=sts1T1E1Status, sts1T1E1Gr303Facility=sts1T1E1Gr303Facility, sts1MapperStatusMultiFErrs=sts1MapperStatusMultiFErrs, sts1VtGroup7=sts1VtGroup7, sts1MapperStatusLOFErrs=sts1MapperStatusLOFErrs, sts1LIUBertDuration=sts1LIUBertDuration, sts1MapperConfigTrap=sts1MapperConfigTrap, dnxSTS1=dnxSTS1, sts1LIUBertErrSecs=sts1LIUBertErrSecs, sts1VtGroup4=sts1VtGroup4, sts1MaprCmdStatus=sts1MaprCmdStatus, VtGroupType=VtGroupType, sts1T1E1IdleCode=sts1T1E1IdleCode, sts1MapperStatusRxTraceErrs=sts1MapperStatusRxTraceErrs, sts1MapperStatusAISErrs=sts1MapperStatusAISErrs, sts1T1E1LinkConfigEntry=sts1T1E1LinkConfigEntry, sts1LIUEntry=sts1LIUEntry, sts1VtGroup3=sts1VtGroup3, sts1LIUCodingViolationErrs=sts1LIUCodingViolationErrs, sts1MapperConfigEntry=sts1MapperConfigEntry, sts1MapperStatusTotErrSecs=sts1MapperStatusTotErrSecs, dnxSTS1Enterprise=dnxSTS1Enterprise, sts1MapperResource=sts1MapperResource, sts1Diag=sts1Diag, sts1LIUDigitalErrs=sts1LIUDigitalErrs, sts1T1E1Clear=sts1T1E1Clear, sts1T1E1RecoverTime=sts1T1E1RecoverTime, sts1T1E1CfgCmdStatus=sts1T1E1CfgCmdStatus, sts1MapperStatusResource=sts1MapperStatusResource, sts1VtGroup1=sts1VtGroup1, sts1T1E1LinkConfigTable=sts1T1E1LinkConfigTable, sts1VtGroup2=sts1VtGroup2, sts1MapperStatusLOSErrs=sts1MapperStatusLOSErrs, sts1MapperStatusAddr=sts1MapperStatusAddr, sts1MapperStatusState=sts1MapperStatusState, sts1T1E1NetLoop=sts1T1E1NetLoop)
