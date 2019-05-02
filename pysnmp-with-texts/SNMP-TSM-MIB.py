#
# PySNMP MIB module SNMP-TSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-TSM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:08:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Counter64, Gauge32, ObjectIdentity, mib_2, Unsigned32, Integer32, IpAddress, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Counter64", "Gauge32", "ObjectIdentity", "mib-2", "Unsigned32", "Integer32", "IpAddress", "ModuleIdentity", "Counter32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
snmpTsmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 190))
snmpTsmMIB.setRevisions(('2009-06-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpTsmMIB.setRevisionsDescriptions(('The initial version, published in RFC 5591.',))
if mibBuilder.loadTexts: snmpTsmMIB.setLastUpdated('200906090000Z')
if mibBuilder.loadTexts: snmpTsmMIB.setOrganization('ISMS Working Group')
if mibBuilder.loadTexts: snmpTsmMIB.setContactInfo('WG-EMail: isms@lists.ietf.org Subscribe: isms-request@lists.ietf.org Chairs: Juergen Quittek NEC Europe Ltd. Network Laboratories Kurfuersten-Anlage 36 69115 Heidelberg Germany +49 6221 90511-15 quittek@netlab.nec.de Juergen Schoenwaelder Jacobs University Bremen Campus Ring 1 28725 Bremen Germany +49 421 200-3587 j.schoenwaelder@jacobs-university.de Editor: David Harrington Huawei Technologies USA 1700 Alma Dr. Plano TX 75075 USA +1 603-436-8634 ietfdbh@comcast.net Wes Hardaker Cobham Analytic Solutions P.O. Box 382 Davis, CA 95617 USA +1 530 792 1913 ietf@hardakers.net ')
if mibBuilder.loadTexts: snmpTsmMIB.setDescription("The Transport Security Model MIB. In keeping with the RFC 3411 design decisions to use self-contained documents, the RFC that contains the definition of this MIB module also includes the elements of procedure that are needed for processing the Transport Security Model for SNMP. These MIB objects SHOULD NOT be modified via other subsystems or models defined in other documents. This allows the Transport Security Model for SNMP to be designed and documented as independent and self-contained, having no direct impact on other modules, and this allows this module to be upgraded and supplemented as the need arises, and to move along the standards track on different time-lines from other modules. Copyright (c) 2009 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: - Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. - Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. - Neither the name of Internet Society, IETF or IETF Trust, nor the names of specific contributors, may be used to endorse or promote products derived from this software without specific prior written permission. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. This version of this MIB module is part of RFC 5591; see the RFC itself for full legal notices.")
snmpTsmNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 0))
snmpTsmMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1))
snmpTsmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2))
snmpTsmStats = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1, 1))
snmpTsmInvalidCaches = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInvalidCaches.setStatus('current')
if mibBuilder.loadTexts: snmpTsmInvalidCaches.setDescription('The number of incoming messages dropped because the tmStateReference referred to an invalid cache. ')
snmpTsmInadequateSecurityLevels = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInadequateSecurityLevels.setStatus('current')
if mibBuilder.loadTexts: snmpTsmInadequateSecurityLevels.setDescription('The number of incoming messages dropped because the securityLevel asserted by the Transport Model was less than the securityLevel requested by the application. ')
snmpTsmUnknownPrefixes = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmUnknownPrefixes.setStatus('current')
if mibBuilder.loadTexts: snmpTsmUnknownPrefixes.setDescription('The number of messages dropped because snmpTsmConfigurationUsePrefix was set to true and there is no known prefix for the specified transport domain. ')
snmpTsmInvalidPrefixes = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInvalidPrefixes.setStatus('current')
if mibBuilder.loadTexts: snmpTsmInvalidPrefixes.setDescription('The number of messages dropped because the securityName associated with an outgoing message did not contain a valid transport domain prefix. ')
snmpTsmConfiguration = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1, 2))
snmpTsmConfigurationUsePrefix = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTsmConfigurationUsePrefix.setStatus('current')
if mibBuilder.loadTexts: snmpTsmConfigurationUsePrefix.setDescription('If this object is set to true, then securityNames passing to and from the application are expected to contain a transport-domain-specific prefix. If this object is set to true, then a domain-specific prefix will be added by the TSM to the securityName for incoming messages and removed from the securityName when processing outgoing messages. Transport domains and prefixes are maintained in a registry by IANA. This object SHOULD persist across system reboots. ')
snmpTsmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2, 1))
snmpTsmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2, 2))
snmpTsmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 190, 2, 1, 1)).setObjects(("SNMP-TSM-MIB", "snmpTsmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpTsmCompliance = snmpTsmCompliance.setStatus('current')
if mibBuilder.loadTexts: snmpTsmCompliance.setDescription('The compliance statement for SNMP engines that support the SNMP-TSM-MIB. ')
snmpTsmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 190, 2, 2, 2)).setObjects(("SNMP-TSM-MIB", "snmpTsmInvalidCaches"), ("SNMP-TSM-MIB", "snmpTsmInadequateSecurityLevels"), ("SNMP-TSM-MIB", "snmpTsmUnknownPrefixes"), ("SNMP-TSM-MIB", "snmpTsmInvalidPrefixes"), ("SNMP-TSM-MIB", "snmpTsmConfigurationUsePrefix"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpTsmGroup = snmpTsmGroup.setStatus('current')
if mibBuilder.loadTexts: snmpTsmGroup.setDescription('A collection of objects for maintaining information of an SNMP engine that implements the SNMP Transport Security Model. ')
mibBuilder.exportSymbols("SNMP-TSM-MIB", snmpTsmConfigurationUsePrefix=snmpTsmConfigurationUsePrefix, snmpTsmMIB=snmpTsmMIB, snmpTsmInvalidCaches=snmpTsmInvalidCaches, snmpTsmCompliance=snmpTsmCompliance, snmpTsmGroup=snmpTsmGroup, snmpTsmUnknownPrefixes=snmpTsmUnknownPrefixes, PYSNMP_MODULE_ID=snmpTsmMIB, snmpTsmStats=snmpTsmStats, snmpTsmInadequateSecurityLevels=snmpTsmInadequateSecurityLevels, snmpTsmCompliances=snmpTsmCompliances, snmpTsmNotifications=snmpTsmNotifications, snmpTsmInvalidPrefixes=snmpTsmInvalidPrefixes, snmpTsmGroups=snmpTsmGroups, snmpTsmConformance=snmpTsmConformance, snmpTsmMIBObjects=snmpTsmMIBObjects, snmpTsmConfiguration=snmpTsmConfiguration)
