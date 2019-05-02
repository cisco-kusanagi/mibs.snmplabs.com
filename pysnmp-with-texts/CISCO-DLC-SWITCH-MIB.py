#
# PySNMP MIB module CISCO-DLC-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DLC-SWITCH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:54:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, iso, NotificationType, Bits, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Gauge32, ModuleIdentity, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "iso", "NotificationType", "Bits", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Gauge32", "ModuleIdentity", "Counter32", "ObjectIdentity")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
ciscoDlcSwitchMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 76))
if mibBuilder.loadTexts: ciscoDlcSwitchMIB.setLastUpdated('9702190000Z')
if mibBuilder.loadTexts: ciscoDlcSwitchMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDlcSwitchMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-fras@cisco.com')
if mibBuilder.loadTexts: ciscoDlcSwitchMIB.setDescription('This is the MIB module for objects used to manage FRAS sessions to the endstation. These objects are specific to downstream or enduster sessions only. It does not contain objects supported by the FRAS-HOST MIB which are specific to upstream or host-end sessions.')
ciscoDlcSwitchMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 76, 1))
frasBnnSdlc = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1))
frasBnnLlc = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2))
frasBanSdlc = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3))
frasBanLlc = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4))
class SAP(TextualConvention, OctetString):
    description = 'Service Access Point - is a term that denotes the means by which a user entity in layer n+1 accesses a service of a provider entity in layer n.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class SdlcAddress(TextualConvention, OctetString):
    description = 'A hexadecimal address assigned to a secondary poll station of an SDLC device.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

frasBnnSdlcConTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1), )
if mibBuilder.loadTexts: frasBnnSdlcConTable.setStatus('current')
if mibBuilder.loadTexts: frasBnnSdlcConTable.setDescription('This table contains mapping information for each SDLC Link Station in a FRAS-BNN to SDLC connection. All entries are derived entirely from the router configuration.')
frasBnnSdlcConEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-DLC-SWITCH-MIB", "bnnSdlcConAddress"))
if mibBuilder.loadTexts: frasBnnSdlcConEntry.setStatus('current')
if mibBuilder.loadTexts: frasBnnSdlcConEntry.setDescription('This table contains the entries defined for a specific SDLC Link Station in a BNN-SDLC configuration.')
bnnSdlcConAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 1), SdlcAddress())
if mibBuilder.loadTexts: bnnSdlcConAddress.setStatus('current')
if mibBuilder.loadTexts: bnnSdlcConAddress.setDescription('This value is the poll address of the secondary link station for this SDLC link. It uniquely identifies the SDLC link station within a single SDLC port.')
bnnSdlcConState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("reset", 1), ("testSent", 2), ("xidexchg", 3), ("connrqsent", 4), ("sigstnwait", 5), ("connrspwait", 6), ("connrspsent", 7), ("contacted", 8), ("discwait", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnnSdlcConState.setStatus('current')
if mibBuilder.loadTexts: bnnSdlcConState.setDescription('Contains the FRAS state of the Link Station. reset - no activity testSent - TEST Frames sent xidexchg - XID exchange in progress connrqsent - Connect request sent sigstnwait - Signal station wait state connrspwait - Connect response wait state connrspsent - Connect response sent contacted - Session established discwait - Disconnect wait state')
bnnSdlcConDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1022))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnnSdlcConDlci.setStatus('current')
if mibBuilder.loadTexts: bnnSdlcConDlci.setDescription('The Data Link Connection Identifier used for this particular connection.')
bnnSdlcConFRInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnnSdlcConFRInterface.setStatus('current')
if mibBuilder.loadTexts: bnnSdlcConFRInterface.setDescription('This is the Frame-Relay interface which the SDLC Link Station is using to connect to the Host.')
bnnSdlcConLocalSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 5), SAP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnnSdlcConLocalSap.setStatus('current')
if mibBuilder.loadTexts: bnnSdlcConLocalSap.setDescription("The Local SAP for this SDLC station's corresponding LLC session to the host.")
bnnSdlcConRemoteSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 6), SAP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnnSdlcConRemoteSap.setStatus('current')
if mibBuilder.loadTexts: bnnSdlcConRemoteSap.setDescription("The Remote SAP for this SDLC station's corresponding LLC session to the host.")
frasBnnLlcConTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1), )
if mibBuilder.loadTexts: frasBnnLlcConTable.setStatus('current')
if mibBuilder.loadTexts: frasBnnLlcConTable.setDescription('This table contains information for each End Station in a FRAS-BNN to LLC connection. The entries are derived entirely from the router configuration.')
frasBnnLlcConEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-DLC-SWITCH-MIB", "bnnLlcConDeviceMacAddress"), (0, "CISCO-DLC-SWITCH-MIB", "bnnLlcConLanLocalSap"), (0, "CISCO-DLC-SWITCH-MIB", "bnnLlcConLanRemoteSap"))
if mibBuilder.loadTexts: frasBnnLlcConEntry.setStatus('current')
if mibBuilder.loadTexts: frasBnnLlcConEntry.setDescription("This table contains information for a specific End Station's connection state in a BNN-LLC connection.")
bnnLlcConDeviceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: bnnLlcConDeviceMacAddress.setStatus('current')
if mibBuilder.loadTexts: bnnLlcConDeviceMacAddress.setDescription("This value is the End Station's Local Mac-Address.")
bnnLlcConLanLocalSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 2), SAP())
if mibBuilder.loadTexts: bnnLlcConLanLocalSap.setStatus('current')
if mibBuilder.loadTexts: bnnLlcConLanLocalSap.setDescription("The End Station's Local SAP.")
bnnLlcConLanRemoteSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 3), SAP())
if mibBuilder.loadTexts: bnnLlcConLanRemoteSap.setStatus('current')
if mibBuilder.loadTexts: bnnLlcConLanRemoteSap.setDescription("The End Station's Remote SAP.")
bnnLlcConLanInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnnLlcConLanInterface.setStatus('current')
if mibBuilder.loadTexts: bnnLlcConLanInterface.setDescription('This is the physical interace which the End Station is attached to.')
bnnLlcConDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1022))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnnLlcConDlci.setStatus('current')
if mibBuilder.loadTexts: bnnLlcConDlci.setDescription('The Data Link Connection Identifier associated with the corresponding LLC2 session over Frame-Relay to the host.')
bnnLlcConState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("reset", 1), ("testSent", 2), ("xidexchg", 3), ("connrqsent", 4), ("sigstnwait", 5), ("connrspwait", 6), ("connrspsent", 7), ("contacted", 8), ("discwait", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnnLlcConState.setStatus('current')
if mibBuilder.loadTexts: bnnLlcConState.setDescription('Contains the FRAS state of the Link Station. reset - no activity testSent - TEST Frames sent xidexchg - XID exchange in progress connrqsent - Connect request sent sigstnwait - Signal station wait state connrspwait - Connect response wait state connrspsent - Connect response sent contacted - Session established discwait - Disconnect wait state')
bnnLlcConLocalMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnnLlcConLocalMacAddress.setStatus('current')
if mibBuilder.loadTexts: bnnLlcConLocalMacAddress.setDescription("The Mac-Address configured as the End Station's target or Remote address.")
bnnLlcConFrLocalSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 8), SAP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnnLlcConFrLocalSap.setStatus('current')
if mibBuilder.loadTexts: bnnLlcConFrLocalSap.setDescription("The FRAS router's Local SAP.")
bnnLlcConFrRemoteSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 9), SAP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bnnLlcConFrRemoteSap.setStatus('current')
if mibBuilder.loadTexts: bnnLlcConFrRemoteSap.setDescription("The FRAS router's Remote SAP.")
frasBanSdlcConTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1), )
if mibBuilder.loadTexts: frasBanSdlcConTable.setStatus('current')
if mibBuilder.loadTexts: frasBanSdlcConTable.setDescription('This table contains information for each SDLC Link Station in a FRAS-BAN to SDLC connection. The entries are derived entirely from the router configuration.')
frasBanSdlcConEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-DLC-SWITCH-MIB", "banSdlcConAddress"), (0, "CISCO-DLC-SWITCH-MIB", "banSdlcConBanDlciMac"))
if mibBuilder.loadTexts: frasBanSdlcConEntry.setStatus('current')
if mibBuilder.loadTexts: frasBanSdlcConEntry.setDescription('This table contains information for a specific SDLC Link Station in a configured for a BAN connection.')
banSdlcConLocalInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banSdlcConLocalInterface.setStatus('current')
if mibBuilder.loadTexts: banSdlcConLocalInterface.setDescription('This is the physical interface the SDLC Link Stations are connected to.')
banSdlcConAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 2), SdlcAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banSdlcConAddress.setStatus('current')
if mibBuilder.loadTexts: banSdlcConAddress.setDescription('This value is the poll address of the secondary link station for this SDLC link. It uniquely identifies the SDLC link station within a single SDLC port.')
banSdlcConBanDlciMac = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banSdlcConBanDlciMac.setStatus('current')
if mibBuilder.loadTexts: banSdlcConBanDlciMac.setDescription("The End Station's target or Remote mac-address.")
banSdlcConDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1022))).setMaxAccess("readonly")
if mibBuilder.loadTexts: banSdlcConDlci.setStatus('current')
if mibBuilder.loadTexts: banSdlcConDlci.setDescription('The Data Link Connection Identifier for the corresponding LLC2 session over Frame-Relay to the host.')
banSdlcConState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("reset", 1), ("testSent", 2), ("xidexchg", 3), ("connrqsent", 4), ("sigstnwait", 5), ("connrspwait", 6), ("connrspsent", 7), ("contacted", 8), ("discwait", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: banSdlcConState.setStatus('current')
if mibBuilder.loadTexts: banSdlcConState.setDescription('Contains the FRAS state of the Link Station. reset - no activity testSent- TEST Frames sent xidexchg - XID exchange in progress connrqsent - Connect request sent sigstnwait - Signal station wait state connrspwait - Connect response wait state connrspsent - Connect response sent contacted - Session established discwait - Disconnect wait state')
banSdlcConVmac = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banSdlcConVmac.setStatus('current')
if mibBuilder.loadTexts: banSdlcConVmac.setDescription("The End Station's virtual Mac-Address which is comprised of a TR formatted template and the SDLC Link Station address appended on the last nibble.")
banSdlcConBniAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banSdlcConBniAddress.setStatus('current')
if mibBuilder.loadTexts: banSdlcConBniAddress.setDescription("BNI is Boundary Node Identifier which is the FRAS-BAN connection's Remote address in TR-format. It is by default 4fff.0000.0000")
banSdlcConFrLocalSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 8), SAP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banSdlcConFrLocalSap.setStatus('current')
if mibBuilder.loadTexts: banSdlcConFrLocalSap.setDescription("The FRAS router's Local SAP.")
banSdlcConFrRemoteSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 9), SAP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banSdlcConFrRemoteSap.setStatus('current')
if mibBuilder.loadTexts: banSdlcConFrRemoteSap.setDescription("The FRAS router's Remote SAP.")
frasBanLlcConTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1), )
if mibBuilder.loadTexts: frasBanLlcConTable.setStatus('current')
if mibBuilder.loadTexts: frasBanLlcConTable.setDescription('This table contains information for each LAN attached End Station in a FRAS-BAN to LAN connection. The entries are from endstations which have their destination mac-addresses as the BAN-DLCI-MAC address.')
frasBanLlcConEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-DLC-SWITCH-MIB", "banLlcEndstnLocalMac"), (0, "CISCO-DLC-SWITCH-MIB", "banLlcConLocalSap"), (0, "CISCO-DLC-SWITCH-MIB", "banLlcConRemoteSap"), (0, "CISCO-DLC-SWITCH-MIB", "banLlcBanDlciMac"))
if mibBuilder.loadTexts: frasBanLlcConEntry.setStatus('current')
if mibBuilder.loadTexts: frasBanLlcConEntry.setDescription('This table contains information for a specific LAN attached End Station.')
banLlcEndstnLocalMac = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banLlcEndstnLocalMac.setStatus('current')
if mibBuilder.loadTexts: banLlcEndstnLocalMac.setDescription("This value is the End Station's Local Mac-Address.")
banLlcBanDlciMac = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banLlcBanDlciMac.setStatus('current')
if mibBuilder.loadTexts: banLlcBanDlciMac.setDescription("This value is the End Station's Remote Mac-Address. It is also the FRAS-BAN connection's Local Mac-Address.")
banLlcConLocalSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 3), SAP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banLlcConLocalSap.setStatus('current')
if mibBuilder.loadTexts: banLlcConLocalSap.setDescription("The endstation's Local SAP.")
banLlcConRemoteSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 4), SAP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banLlcConRemoteSap.setStatus('current')
if mibBuilder.loadTexts: banLlcConRemoteSap.setDescription("The endstation's Remote SAP.")
banLlcConDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 1022))).setMaxAccess("readonly")
if mibBuilder.loadTexts: banLlcConDlci.setStatus('current')
if mibBuilder.loadTexts: banLlcConDlci.setDescription('The Data Link Connection Identifier associated with the corresponding LLC2 session over Frame-Relay to the host.')
banLlcConState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("reset", 1), ("testSent", 2), ("xidexchg", 3), ("connrqsent", 4), ("sigstnwait", 5), ("connrspwait", 6), ("connrspsent", 7), ("contacted", 8), ("discwait", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: banLlcConState.setStatus('current')
if mibBuilder.loadTexts: banLlcConState.setDescription('Contains the FRAS state of the Link Station. reset - no activity testSent- TEST Frames sent xidexchg - XID exchange in progress connrqsent - Connect request sent sigstnwait - Signal station wait state connrspwait - Connect response wait state connrspsent - Connect response sent contacted - Session established discwait - Disconnect wait state')
banLlcConFrInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banLlcConFrInterface.setStatus('current')
if mibBuilder.loadTexts: banLlcConFrInterface.setDescription('This is the Frame-Relay interface for this particular session.')
banLlcBniAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 8), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banLlcBniAddress.setStatus('current')
if mibBuilder.loadTexts: banLlcBniAddress.setDescription("This value is the FRAS-BAN connection's Target Mac-Address. It is by default 4fff.0000.0000")
banLlcConFrLocalSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 9), SAP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banLlcConFrLocalSap.setStatus('current')
if mibBuilder.loadTexts: banLlcConFrLocalSap.setDescription('The Local SAP of the corresponding LLC2 session over Frame-Relay to the host.')
banLlcConFrRemoteSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 10), SAP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: banLlcConFrRemoteSap.setStatus('current')
if mibBuilder.loadTexts: banLlcConFrRemoteSap.setDescription('The Remote SAP of the corresponding LLC2 session over Frame-Relay to the host.')
ciscoDlcSwitchConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 76, 2))
ciscoDlcSwitchCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 1))
ciscoDlcSwitchGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2))
ciscoDlcSwitchCoreCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 1, 1)).setObjects(("CISCO-DLC-SWITCH-MIB", "frasBnnSdlcGroup"), ("CISCO-DLC-SWITCH-MIB", "frasBnnLlcGroup"), ("CISCO-DLC-SWITCH-MIB", "frasBanSdlcGroup"), ("CISCO-DLC-SWITCH-MIB", "frasBanLlcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDlcSwitchCoreCompliance = ciscoDlcSwitchCoreCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoDlcSwitchCoreCompliance.setDescription('The core compliance statement for all FRAS connections.')
frasBnnSdlcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 1)).setObjects(("CISCO-DLC-SWITCH-MIB", "bnnSdlcConState"), ("CISCO-DLC-SWITCH-MIB", "bnnSdlcConDlci"), ("CISCO-DLC-SWITCH-MIB", "bnnSdlcConFRInterface"), ("CISCO-DLC-SWITCH-MIB", "bnnSdlcConLocalSap"), ("CISCO-DLC-SWITCH-MIB", "bnnSdlcConRemoteSap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frasBnnSdlcGroup = frasBnnSdlcGroup.setStatus('current')
if mibBuilder.loadTexts: frasBnnSdlcGroup.setDescription('The frasBnnSdlcGroup defines objects which are common to the BNN SDLC of all compliant connections.')
frasBnnLlcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 2)).setObjects(("CISCO-DLC-SWITCH-MIB", "bnnLlcConLanInterface"), ("CISCO-DLC-SWITCH-MIB", "bnnLlcConDlci"), ("CISCO-DLC-SWITCH-MIB", "bnnLlcConState"), ("CISCO-DLC-SWITCH-MIB", "bnnLlcConLocalMacAddress"), ("CISCO-DLC-SWITCH-MIB", "bnnLlcConFrLocalSap"), ("CISCO-DLC-SWITCH-MIB", "bnnLlcConFrRemoteSap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frasBnnLlcGroup = frasBnnLlcGroup.setStatus('current')
if mibBuilder.loadTexts: frasBnnLlcGroup.setDescription('The frasBnnLlcGroup defines objects which are common to the BNN LLC of all compliant connections.')
frasBanSdlcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 3)).setObjects(("CISCO-DLC-SWITCH-MIB", "banSdlcConLocalInterface"), ("CISCO-DLC-SWITCH-MIB", "banSdlcConAddress"), ("CISCO-DLC-SWITCH-MIB", "banSdlcConBanDlciMac"), ("CISCO-DLC-SWITCH-MIB", "banSdlcConDlci"), ("CISCO-DLC-SWITCH-MIB", "banSdlcConState"), ("CISCO-DLC-SWITCH-MIB", "banSdlcConVmac"), ("CISCO-DLC-SWITCH-MIB", "banSdlcConBniAddress"), ("CISCO-DLC-SWITCH-MIB", "banSdlcConFrLocalSap"), ("CISCO-DLC-SWITCH-MIB", "banSdlcConFrRemoteSap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frasBanSdlcGroup = frasBanSdlcGroup.setStatus('current')
if mibBuilder.loadTexts: frasBanSdlcGroup.setDescription('The frasBanSdlcGroup defines objects which are common to the BAN SDLC of all compliant connections.')
frasBanLlcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 4)).setObjects(("CISCO-DLC-SWITCH-MIB", "banLlcEndstnLocalMac"), ("CISCO-DLC-SWITCH-MIB", "banLlcBanDlciMac"), ("CISCO-DLC-SWITCH-MIB", "banLlcConDlci"), ("CISCO-DLC-SWITCH-MIB", "banLlcConLocalSap"), ("CISCO-DLC-SWITCH-MIB", "banLlcConRemoteSap"), ("CISCO-DLC-SWITCH-MIB", "banLlcConState"), ("CISCO-DLC-SWITCH-MIB", "banLlcConFrInterface"), ("CISCO-DLC-SWITCH-MIB", "banLlcBniAddress"), ("CISCO-DLC-SWITCH-MIB", "banLlcConFrLocalSap"), ("CISCO-DLC-SWITCH-MIB", "banLlcConFrRemoteSap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    frasBanLlcGroup = frasBanLlcGroup.setStatus('current')
if mibBuilder.loadTexts: frasBanLlcGroup.setDescription('The frasBanLlcGroup defines objects which are common to the BAN LLC of all compliant connections.')
mibBuilder.exportSymbols("CISCO-DLC-SWITCH-MIB", ciscoDlcSwitchMIB=ciscoDlcSwitchMIB, frasBnnLlcConEntry=frasBnnLlcConEntry, ciscoDlcSwitchGroups=ciscoDlcSwitchGroups, banLlcConFrLocalSap=banLlcConFrLocalSap, banLlcConState=banLlcConState, ciscoDlcSwitchCoreCompliance=ciscoDlcSwitchCoreCompliance, frasBanLlcGroup=frasBanLlcGroup, bnnSdlcConRemoteSap=bnnSdlcConRemoteSap, PYSNMP_MODULE_ID=ciscoDlcSwitchMIB, banSdlcConAddress=banSdlcConAddress, bnnLlcConDlci=bnnLlcConDlci, bnnSdlcConState=bnnSdlcConState, bnnLlcConLanRemoteSap=bnnLlcConLanRemoteSap, banLlcBanDlciMac=banLlcBanDlciMac, frasBanLlc=frasBanLlc, bnnSdlcConAddress=bnnSdlcConAddress, banSdlcConVmac=banSdlcConVmac, frasBanSdlcGroup=frasBanSdlcGroup, frasBnnSdlcConTable=frasBnnSdlcConTable, banSdlcConDlci=banSdlcConDlci, frasBanLlcConTable=frasBanLlcConTable, frasBnnSdlcConEntry=frasBnnSdlcConEntry, frasBanSdlcConEntry=frasBanSdlcConEntry, frasBnnLlcConTable=frasBnnLlcConTable, bnnSdlcConLocalSap=bnnSdlcConLocalSap, bnnLlcConFrRemoteSap=bnnLlcConFrRemoteSap, frasBnnLlcGroup=frasBnnLlcGroup, bnnLlcConFrLocalSap=bnnLlcConFrLocalSap, SdlcAddress=SdlcAddress, banSdlcConBanDlciMac=banSdlcConBanDlciMac, banLlcEndstnLocalMac=banLlcEndstnLocalMac, ciscoDlcSwitchMIBObjects=ciscoDlcSwitchMIBObjects, SAP=SAP, banSdlcConFrRemoteSap=banSdlcConFrRemoteSap, ciscoDlcSwitchConformance=ciscoDlcSwitchConformance, banLlcConDlci=banLlcConDlci, banLlcBniAddress=banLlcBniAddress, frasBnnSdlcGroup=frasBnnSdlcGroup, bnnLlcConLocalMacAddress=bnnLlcConLocalMacAddress, banSdlcConState=banSdlcConState, frasBanSdlcConTable=frasBanSdlcConTable, frasBanSdlc=frasBanSdlc, bnnLlcConState=bnnLlcConState, banSdlcConBniAddress=banSdlcConBniAddress, bnnLlcConDeviceMacAddress=bnnLlcConDeviceMacAddress, banLlcConFrRemoteSap=banLlcConFrRemoteSap, bnnSdlcConDlci=bnnSdlcConDlci, banSdlcConLocalInterface=banSdlcConLocalInterface, banLlcConFrInterface=banLlcConFrInterface, bnnSdlcConFRInterface=bnnSdlcConFRInterface, bnnLlcConLanInterface=bnnLlcConLanInterface, banLlcConRemoteSap=banLlcConRemoteSap, frasBnnLlc=frasBnnLlc, banSdlcConFrLocalSap=banSdlcConFrLocalSap, ciscoDlcSwitchCompliances=ciscoDlcSwitchCompliances, frasBanLlcConEntry=frasBanLlcConEntry, bnnLlcConLanLocalSap=bnnLlcConLanLocalSap, banLlcConLocalSap=banLlcConLocalSap, frasBnnSdlc=frasBnnSdlc)
