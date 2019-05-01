#
# PySNMP MIB module ENTERASYS-AAA-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-AAA-POLICY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Integer32, TimeTicks, Counter64, Counter32, iso, NotificationType, ObjectIdentity, Unsigned32, IpAddress, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Integer32", "TimeTicks", "Counter64", "Counter32", "iso", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "Gauge32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysAAAPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51))
etsysAAAPolicyMIB.setRevisions(('2004-07-29 19:06',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysAAAPolicyMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysAAAPolicyMIB.setLastUpdated('200407291906Z')
if mibBuilder.loadTexts: etsysAAAPolicyMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysAAAPolicyMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysAAAPolicyMIB.setDescription('This MIB module defines a portion of the SNMP MIB under the Enterasys Networks enterprise OID pertaining to the configuration of authentications services.')
class AAAProtocol(TextualConvention, Integer32):
    description = 'The remote AAA protocols that can be selected for providing specific AAA services. any(1) - Any, but only one, of the configured remote AAA protocols will be used. none(2) - No remote AAA protocol will be used. radius(3) - RADIUS will be used. tacacs(4) - TACACS+ will be used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("any", 1), ("none", 2), ("radius", 3), ("tacacs", 4))

etsysAAAPolicyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1))
etsysAAAPolicyMgmtAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1))
etsysAAAMgmtAccessTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1), )
if mibBuilder.loadTexts: etsysAAAMgmtAccessTable.setStatus('current')
if mibBuilder.loadTexts: etsysAAAMgmtAccessTable.setDescription('A table of supported management access protocols and their corresponding authentication, authorization, and accounting (AAA) protocols. Maintaining the values of the objects in this table across agent reboots is REQUIRED.')
etsysAAAMgmtAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1), ).setIndexNames((0, "ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtAccessProtocol"))
if mibBuilder.loadTexts: etsysAAAMgmtAccessEntry.setStatus('current')
if mibBuilder.loadTexts: etsysAAAMgmtAccessEntry.setDescription('A particular management access protocol and the remote AAA protocol that should be used to authenticate users requesting access via that protocol.')
etsysAAAMgmtAccessProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("allProtocols", 1))))
if mibBuilder.loadTexts: etsysAAAMgmtAccessProtocol.setStatus('current')
if mibBuilder.loadTexts: etsysAAAMgmtAccessProtocol.setDescription('The management protocol that is represented by this row. The values of this parameter are as follows: allProtocols(1) - all management access protocols.')
etsysAAAMgmtRemoteAuthProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 2), AAAProtocol().clone('any')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAAAMgmtRemoteAuthProtocol.setStatus('current')
if mibBuilder.loadTexts: etsysAAAMgmtRemoteAuthProtocol.setDescription('The type of remote AAA protocol to be used for authenticating users seeking management access via the associated protocol. When this object has the default value of any(1) the remote AAA protocol will be selected using the following precedence order TACACS+, RADIUS. A protocol will be selected if, and only if, it is enabled. When a remote authentication protocol has been consulted, and the protocol times out, the local password file will be used to authenticate the user. If no remote AAA protocol is selected, or the selected remote AAA protocol is not enabled, the local password file will be used to authenticate the user.')
etsysAAAMgmtRemoteAcctProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 1, 1, 1, 1, 3), AAAProtocol().clone('any')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAAAMgmtRemoteAcctProtocol.setStatus('current')
if mibBuilder.loadTexts: etsysAAAMgmtRemoteAcctProtocol.setDescription('The type of remote AAA protocol to be used for handling the accounting information related to management accesses via the associated protocol. When this object has the default value of any(1) the remote AAA protocol will be selected using the following precedence order RADIUS, TACACS+. A protocol will be selected if, and only if, it is enabled.')
etsysAAAPolicyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2))
etsysAAAPolicyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 1))
etsysAAAPolicyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 2))
etsysAAAPolicyMgmtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 2, 1)).setObjects(("ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtRemoteAuthProtocol"), ("ENTERASYS-AAA-POLICY-MIB", "etsysAAAMgmtRemoteAcctProtocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAAAPolicyMgmtGroup = etsysAAAPolicyMgmtGroup.setStatus('current')
if mibBuilder.loadTexts: etsysAAAPolicyMgmtGroup.setDescription('The basic collection of objects providing proprietary management of the authentication policy for management protocols of the managed entity.')
etsysAAAPolicyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 51, 2, 1, 1)).setObjects(("ENTERASYS-AAA-POLICY-MIB", "etsysAAAPolicyMgmtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAAAPolicyMIBCompliance = etsysAAAPolicyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysAAAPolicyMIBCompliance.setDescription('The compliance statement for Managed entities implementing the Enterasys AAA Policy MIB.')
mibBuilder.exportSymbols("ENTERASYS-AAA-POLICY-MIB", etsysAAAPolicyMIBConformance=etsysAAAPolicyMIBConformance, etsysAAAMgmtRemoteAuthProtocol=etsysAAAMgmtRemoteAuthProtocol, etsysAAAPolicyMIBGroups=etsysAAAPolicyMIBGroups, etsysAAAPolicyObjects=etsysAAAPolicyObjects, etsysAAAMgmtAccessTable=etsysAAAMgmtAccessTable, etsysAAAMgmtAccessEntry=etsysAAAMgmtAccessEntry, etsysAAAPolicyMIBCompliance=etsysAAAPolicyMIBCompliance, PYSNMP_MODULE_ID=etsysAAAPolicyMIB, etsysAAAPolicyMgmtAccess=etsysAAAPolicyMgmtAccess, AAAProtocol=AAAProtocol, etsysAAAMgmtRemoteAcctProtocol=etsysAAAMgmtRemoteAcctProtocol, etsysAAAPolicyMgmtGroup=etsysAAAPolicyMgmtGroup, etsysAAAPolicyMIB=etsysAAAPolicyMIB, etsysAAAPolicyMIBCompliances=etsysAAAPolicyMIBCompliances, etsysAAAMgmtAccessProtocol=etsysAAAMgmtAccessProtocol)
